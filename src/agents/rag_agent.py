"""
rag_agent.py — Agente RAG genérico reutilizado por los agentes especializados.

Cada agente especializado (RR.HH., Tecnología, Finanzas) es una *instancia* de
RAGAgent con su propio vector store, su rol (system prompt) y su dominio. La
cadena se construye con LCEL (LangChain Expression Language):

    {question} -> retriever -> formato de contexto -> prompt -> LLM -> parser

El agente SOLO responde con lo que está en sus documentos (grounding) y avisa
cuando la documentación no alcanza, en lugar de inventar (anti-alucinación).
"""

from typing import Any, Dict, List

from langchain_chroma import Chroma
from langchain_core.documents import Document
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import Runnable, RunnableLambda, RunnablePassthrough
from langchain_openai import ChatOpenAI

from src import config

RAG_PROMPT = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "Sos {role}. Respondé en español, de forma clara y concreta, usando "
            "EXCLUSIVAMENTE el contexto provisto de la documentación interna de Nimbus Cloud. "
            "Si el contexto no contiene la respuesta, decí explícitamente que no encontraste "
            "esa información en la documentación y sugerí contactar al área ({contact}). "
            "No inventes datos, plazos ni montos.",
        ),
        ("human", "CONTEXTO:\n{context}\n\nPREGUNTA: {question}"),
    ]
)


def format_context(docs: List[Document]) -> str:
    """Convierte los chunks recuperados en un bloque de texto con su fuente."""
    return "\n\n".join(f"[{d.metadata.get('source', '?')}] {d.page_content}" for d in docs)


class RAGAgent:
    """Agente especializado: retriever propio + prompt de rol + LLM."""

    def __init__(self, name: str, domain: str, role: str, contact: str, vector_store: Chroma, llm: ChatOpenAI):
        self.name = name
        self.domain = domain
        self.role = role
        self.contact = contact
        self.retriever = vector_store.as_retriever(search_kwargs={"k": config.TOP_K})
        self.llm = llm
        self.chain: Runnable = self._build_chain()

    def _build_chain(self) -> Runnable:
        """Cadena LCEL: recupera, formatea, genera. Devuelve answer + fuentes (para auditar)."""

        def retrieve(inputs: Dict[str, Any]) -> Dict[str, Any]:
            docs = self.retriever.invoke(inputs["question"])
            return {**inputs, "docs": docs, "context": format_context(docs)}

        def to_result(inputs: Dict[str, Any]) -> Dict[str, Any]:
            return {
                "agent": self.name,
                "domain": self.domain,
                "question": inputs["question"],
                "answer": inputs["answer"],
                "context": inputs["context"],
                "sources": sorted({d.metadata.get("source", "?") for d in inputs["docs"]}),
                "num_chunks": len(inputs["docs"]),
            }

        generate = RAG_PROMPT | self.llm | StrOutputParser()

        main_chain = (
            RunnableLambda(retrieve).with_config(run_name=f"{self.name}:retrieve")
            | RunnablePassthrough.assign(role=lambda _: self.role, contact=lambda _: self.contact)
            | RunnablePassthrough.assign(answer=generate.with_config(run_name=f"{self.name}:generate"))
            | RunnableLambda(to_result).with_config(run_name=f"{self.name}:result")
        ).with_config(run_name=self.name)

        # Manejo de errores (L4): si algo falla dentro del agente, NO se pierde la consulta ni se
        # "rebota" a otro agente: se devuelve un mensaje claro al usuario y el error queda en la traza.
        def error_result(inputs: Dict[str, Any]) -> Dict[str, Any]:
            return {
                "agent": self.name,
                "domain": self.domain,
                "question": inputs["question"],
                "answer": (
                    "No pudimos resolver tu consulta en este momento. "
                    f"Nuestro equipo te dará seguimiento en breve ({self.contact})."
                ),
                "context": "",
                "sources": [],
                "num_chunks": 0,
                "error": repr(inputs.get("error")),
            }

        return main_chain.with_fallbacks(
            [RunnableLambda(error_result).with_config(run_name=f"{self.name}:error-fallback")],
            exception_key="error",
        )

    def invoke(self, question: str, config_: Any = None) -> Dict[str, Any]:
        return self.chain.invoke({"question": question}, config=config_)
