"""
multi_agent_system.py — Sistema multiagente completo (orquestador + agentes RAG + trazas + evaluador).

Flujo de UNA consulta (todo queda en una única traza de Langfuse):

    consulta
       │
       ▼
  [Orquestador]  clasifica la intención -> RoutingDecision (1..3 rutas)
       │
       ▼   enrutamiento condicional (RunnableBranch), en paralelo si hay varias rutas
  [Agente HR] / [Agente TECH] / [Agente FINANCE] / [Fallback OUT_OF_SCOPE]
       │         (cada uno: retriever propio -> prompt -> LLM)
       ▼
  respuesta final  ──►  [Evaluador]  puntaje 1-10  ──►  Score API de Langfuse
"""

import time
import uuid
from typing import Any, Dict, List, Optional

from langchain_core.runnables import RunnableBranch, RunnableLambda
from langchain_openai import ChatOpenAI

from src import config, tracing
from src.agents.finance_agent import create_finance_agent
from src.agents.hr_agent import create_hr_agent
from src.agents.orchestrator import RoutingDecision, Route, create_orchestrator
from src.agents.tech_agent import create_tech_agent
from src.evaluator import create_evaluator, evaluate_response, log_scores_to_langfuse, scores_to_dict
from src.knowledge_base import build_all_vector_stores

DEPARTMENT_LABELS = {"HR": "Recursos Humanos", "TECH": "Soporte Técnico", "FINANCE": "Finanzas"}

OUT_OF_SCOPE_MESSAGE = (
    "Tu consulta no corresponde a ninguna de las áreas que atiende este asistente "
    "(Recursos Humanos, Soporte Técnico o Finanzas). Si es un tema interno de Nimbus Cloud, "
    "reformulá la pregunta indicando el área o escribí a people@nimbuscloud.example."
)


class SupportSystem:
    """Fachada del sistema: construye vector stores, agentes, orquestador y evaluador."""

    def __init__(self, rebuild_index: bool = False, evaluate: bool = True):
        config.require_openai_key()
        self.evaluate = evaluate
        self.llm = ChatOpenAI(model=config.CHAT_MODEL, temperature=0, api_key=config.require_openai_key())
        self.vector_stores = build_all_vector_stores(rebuild=rebuild_index)

        self.agents = {
            "HR": create_hr_agent(self.vector_stores["HR"], self.llm),
            "TECH": create_tech_agent(self.vector_stores["TECH"], self.llm),
            "FINANCE": create_finance_agent(self.vector_stores["FINANCE"], self.llm),
        }
        self.orchestrator = create_orchestrator(self.llm)
        self.evaluator = create_evaluator(self.llm)
        self.agent_router = self._build_router()

    # ------------------------------------------------------------------ routing
    def _build_router(self) -> RunnableBranch:
        """Enrutamiento condicional: según `department` se ejecuta la cadena del agente correcto."""

        def out_of_scope(inputs: Dict[str, Any]) -> Dict[str, Any]:
            return {
                "agent": "fallback",
                "domain": "OUT_OF_SCOPE",
                "question": inputs["question"],
                "answer": OUT_OF_SCOPE_MESSAGE,
                "context": "",
                "sources": [],
                "num_chunks": 0,
            }

        return RunnableBranch(
            (lambda x: x["department"] == "HR", self.agents["HR"].chain),
            (lambda x: x["department"] == "TECH", self.agents["TECH"].chain),
            (lambda x: x["department"] == "FINANCE", self.agents["FINANCE"].chain),
            RunnableLambda(out_of_scope).with_config(run_name="out-of-scope-fallback"),
        ).with_config(run_name="router:conditional_branch")

    def classify(self, question: str, config_: Any = None) -> RoutingDecision:
        """Llama al orquestador; ante un error devuelve OUT_OF_SCOPE con confianza 0 (falla seguro)."""
        try:
            decision = self.orchestrator.invoke({"question": question}, config=config_)
            if not decision.routes:
                raise ValueError("el orquestador no devolvió rutas")
            return decision
        except Exception as exc:  # noqa: BLE001 — registrado en reasoning y en la traza
            return RoutingDecision(
                routes=[Route(department="OUT_OF_SCOPE", sub_question=question)],
                confidence=0.0,
                reasoning=f"Error del orquestador: {exc}",
            )

    # ------------------------------------------------------------------ main API
    def answer(
        self,
        question: str,
        session_id: Optional[str] = None,
        user_id: Optional[str] = None,
        expected_intent: Optional[List[str]] = None,
        run_tag: Optional[str] = None,
    ) -> Dict[str, Any]:
        """Procesa una consulta de punta a punta y devuelve un dict auditable."""
        started = time.time()
        session_id = session_id or f"session-{uuid.uuid4().hex[:8]}"

        with tracing.traced_run(
            "support-query",
            {"question": question},
            session_id=session_id,
            user_id=user_id,
            tags=["m3-multiagent"] + ([run_tag] if run_tag else []),
        ) as (handler, trace_id, root):
            cfg = {"callbacks": [handler]} if handler else {}

            decision = self.classify(question, cfg)
            routes = self._merge_routes(decision.routes)
            inputs = [{"department": r.department, "question": r.sub_question} for r in routes]

            # Metadata para depurar misclassifications en Langfuse (filtrar por tag / comparar intents)
            actual = [r.department for r in routes]
            tags = [f"dept:{d}" for d in actual]
            meta = {"actual_intent": ",".join(actual), "router_confidence": f"{decision.confidence:.2f}"}
            if expected_intent:
                meta["expected_intent"] = ",".join(expected_intent)
                if not all(d in expected_intent for d in actual):
                    tags.append("misclassified")
            with tracing.trace_attributes(tags=tags, metadata=meta):
                results: List[Dict[str, Any]] = self.agent_router.batch(inputs, config=cfg)  # en paralelo

            final_answer = self._combine(results)
            evaluation = self._evaluate(question, results, cfg, trace_id)

            output = {
                "question": question,
                "routing": {
                    "departments": [r.department for r in routes],
                    "confidence": decision.confidence,
                    "reasoning": decision.reasoning,
                    "routes": [r.model_dump() for r in routes],
                },
                "answer": final_answer,
                "agents_used": [r["agent"] for r in results],
                "sources": sorted({s for r in results for s in r["sources"]}),
                "evaluation": evaluation,
                "trace_id": trace_id,
                "latency_s": round(time.time() - started, 2),
            }
            if root is not None:
                root.update(
                    output={"answer": final_answer, "routing": output["routing"], "evaluation": evaluation},
                    metadata=meta,
                )
                client = tracing.get_langfuse()
                output["trace_url"] = client.get_trace_url(trace_id=trace_id) if client else None

        tracing.flush()
        return output

    # ------------------------------------------------------------------ helpers
    @staticmethod
    def _merge_routes(routes: List[Route]) -> List[Route]:
        """Una sola ruta por área (se unen sub-preguntas repetidas); sin OUT_OF_SCOPE mezclado; máx. 3."""
        # Guarda determinista: OUT_OF_SCOPE nunca se mezcla con áreas reales (si hay áreas reales, se descarta)
        real = [r for r in routes if r.department != "OUT_OF_SCOPE"]
        routes = real or routes[:1]
        merged: Dict[str, Route] = {}
        for r in routes:
            if r.department in merged:
                prev = merged[r.department]
                merged[r.department] = Route(department=r.department, sub_question=f"{prev.sub_question} {r.sub_question}")
            else:
                merged[r.department] = r
        return list(merged.values())[:3]

    @staticmethod
    def _combine(results: List[Dict[str, Any]]) -> str:
        """Una respuesta por área; si hay varias, se presentan con su encabezado."""
        if len(results) == 1:
            return results[0]["answer"]
        parts = [f"**{DEPARTMENT_LABELS.get(r['domain'], r['domain'])}**\n{r['answer']}" for r in results]
        return "\n\n".join(parts)

    def _evaluate(self, question: str, results: List[Dict[str, Any]], cfg: Dict[str, Any], trace_id: Optional[str]):
        """Evalúa cada respuesta RAG (no el fallback) y registra el puntaje global en Langfuse."""
        if not self.evaluate:
            return None
        rag_results = [r for r in results if r["agent"] != "fallback" and not r.get("error")]
        if not rag_results:
            return None
        per_agent = []
        for r in rag_results:
            scores = evaluate_response(self.evaluator, r["question"], r["answer"], r["context"], cfg)
            per_agent.append((r["agent"], scores))
        # puntaje de la traza = promedio de los agentes involucrados
        avg = lambda attr: max(1, min(10, round(sum(getattr(s, attr) for _, s in per_agent) / len(per_agent))))  # noqa: E731
        merged = per_agent[0][1].model_copy(
            update={
                "relevance": avg("relevance"),
                "completeness": avg("completeness"),
                "accuracy": avg("accuracy"),
                "overall": avg("overall"),
                "reason": " | ".join(f"{name}: {s.reason}" for name, s in per_agent),
            }
        )
        log_scores_to_langfuse(trace_id, merged)
        out = scores_to_dict(merged)
        out["per_agent"] = {name: s.model_dump() for name, s in per_agent}
        return out
