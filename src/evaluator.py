"""
evaluator.py — (BONUS) Agente Evaluador con la Score API de Langfuse.

Un LLM-as-judge puntúa cada respuesta RAG de 1 a 10 a partir de la consulta original,
la respuesta final y el contexto recuperado, en tres dimensiones:
  * relevance     — ¿la respuesta atiende lo que se preguntó?
  * completeness  — ¿cubre todos los aspectos de la pregunta?
  * accuracy      — ¿es fiel al contexto recuperado (sin inventar datos)?
más un puntaje global `quality` (1-10).

Los puntajes se registran en la traza correspondiente con `langfuse.create_score(...)`
(Score API), por lo que quedan visibles en Langfuse (Traces -> Scores) y pueden usarse
para filtrar respuestas de baja calidad y armar dashboards de calidad continuos.
"""

from typing import Any, Dict, Optional

from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from pydantic import BaseModel, Field

from src import tracing

QUALITY_THRESHOLD = 6  # por debajo de este puntaje global, la respuesta se marca como "baja calidad"


class QualityScores(BaseModel):
    relevance: int = Field(ge=1, le=10, description="Relevancia de la respuesta respecto de la consulta (1-10).")
    completeness: int = Field(ge=1, le=10, description="Completitud: cubre todo lo preguntado (1-10).")
    accuracy: int = Field(ge=1, le=10, description="Exactitud/fidelidad al contexto recuperado, sin inventar (1-10).")
    overall: int = Field(ge=1, le=10, description="Puntaje global de calidad (1-10).")
    reason: str = Field(description="Justificación concreta de los puntajes (2-3 frases).")


JUDGE_PROMPT = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "Sos un evaluador estricto de calidad de respuestas de un sistema RAG de soporte interno. "
            "Recibís la consulta original, el contexto recuperado de la documentación y la respuesta final. "
            "Puntuá de 1 a 10 (10 = excelente): relevance, completeness y accuracy (fidelidad al contexto: "
            "penalizá fuerte datos que NO estén en el contexto) y un overall global. "
            "Si la respuesta dice correctamente que la documentación no contiene la información, "
            "accuracy puede ser alta pero completeness debe ser baja. Justificá brevemente.",
        ),
        ("human", "CONSULTA:\n{question}\n\nCONTEXTO RECUPERADO:\n{context}\n\nRESPUESTA FINAL:\n{answer}"),
    ]
)


def create_evaluator(llm: ChatOpenAI):
    """Cadena LCEL del juez: prompt -> LLM con salida estructurada (QualityScores)."""
    return (JUDGE_PROMPT | llm.with_structured_output(QualityScores)).with_config(run_name="evaluator:judge")


def evaluate_response(evaluator, question: str, answer: str, context: str, config_: Any = None) -> QualityScores:
    return evaluator.invoke({"question": question, "answer": answer, "context": context}, config=config_)


def log_scores_to_langfuse(trace_id: Optional[str], scores: QualityScores) -> bool:
    """Registra los 4 puntajes en la traza vía la Score API. Devuelve False si no hay Langfuse."""
    client = tracing.get_langfuse()
    if client is None or not trace_id:
        return False
    for name, value in (
        ("quality", scores.overall),
        ("relevance", scores.relevance),
        ("completeness", scores.completeness),
        ("accuracy", scores.accuracy),
    ):
        client.create_score(
            trace_id=trace_id,
            name=name,
            value=float(value),
            data_type="NUMERIC",
            comment=scores.reason if name == "quality" else None,
        )
    return True


def scores_to_dict(scores: QualityScores) -> Dict[str, Any]:
    d = scores.model_dump()
    d["low_quality"] = scores.overall < QUALITY_THRESHOLD
    return d
