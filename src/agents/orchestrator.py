"""
orchestrator.py — Agente Orquestador (clasificación de intención + routing).

El orquestador NO responde preguntas: sólo analiza la consulta y decide a qué
agente(s) especialista(s) delegarla (L3: roles claros + delegación).

Usa salida estructurada (Pydantic + `with_structured_output`) para obtener una
decisión determinista y validada, en vez de parsear texto libre. Soporta:
  * ruteo directo (una consulta -> un agente),
  * delegación en paralelo (una consulta con sub-preguntas de varias áreas),
  * OUT_OF_SCOPE (consultas que no son de ningún área: no se inventa respuesta).
"""

from typing import List, Literal

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import Runnable
from langchain_openai import ChatOpenAI
from pydantic import BaseModel, Field

Department = Literal["HR", "TECH", "FINANCE", "OUT_OF_SCOPE"]


class Route(BaseModel):
    """Una delegación: qué área atiende qué sub-pregunta."""

    department: Department = Field(description="Área responsable de esta (sub)pregunta.")
    sub_question: str = Field(description="La parte de la consulta que le corresponde a esa área, autocontenida.")


class RoutingDecision(BaseModel):
    """Decisión completa del orquestador (se registra en la traza de Langfuse)."""

    routes: List[Route] = Field(
        description="Una ruta por cada área involucrada (máximo 3). Si la consulta no es de ningún área, una sola ruta OUT_OF_SCOPE."
    )
    confidence: float = Field(ge=0.0, le=1.0, description="Confianza de la clasificación entre 0 y 1.")
    reasoning: str = Field(description="Justificación breve (1-2 frases) de por qué se eligió ese ruteo.")


ORCHESTRATOR_SYSTEM_PROMPT = """Sos el Agente Orquestador del sistema de soporte interno de Nimbus Cloud.
Tu único trabajo es CLASIFICAR la intención de la consulta y decidir a qué agente especialista delegarla.
No respondas la consulta.

Áreas disponibles:
- HR: recursos humanos — vacaciones, licencias, beneficios, aguinaldo/bono, onboarding, evaluaciones de desempeño, carrera, trabajo remoto, conducta, renuncia/offboarding.
- TECH: soporte técnico/IT — contraseñas, cuentas, accesos, VPN, MFA, laptops y equipamiento, software y licencias, red/Wi-Fi, tickets y SLAs de IT, seguridad informática.
- FINANCE: finanzas — gastos y reembolsos, tarjetas corporativas, facturación a clientes, cobranzas, compras y proveedores, presupuesto, cierre contable, pagos y recibos de sueldo (aspecto contable/pago).
- OUT_OF_SCOPE: cualquier cosa que no encaje en las áreas anteriores (clima, recetas, política, chistes, conocimiento general).

Reglas:
1. Elegí el área por el TEMA principal de la consulta, no por palabras sueltas (ej.: "reembolso del internet de home office" es FINANCE si pregunta cómo se reintegra/paga; "beneficio de internet" es HR).
2. Si la consulta contiene preguntas independientes de áreas DISTINTAS, devolvé una ruta por área con su sub_question propia (máximo 3). NUNCA repitas un área: si varias partes son del mismo área, usá una sola ruta con toda la consulta de esa área.
3. Si es ambigua, elegí el área más probable y bajá la confianza (< 0.6).
4. Usá OUT_OF_SCOPE SOLO si TODA la consulta es ajena a las áreas, y siempre como única ruta; nunca la combines con otras áreas. Los trámites internos hechos 'en el portal' (cargar una licencia, pedir un reembolso, abrir un ticket) pertenecen al área del trámite, no son OUT_OF_SCOPE.
5. Cada sub_question debe poder entenderse sola (sin depender del resto del mensaje)."""


def create_orchestrator(llm: ChatOpenAI) -> Runnable:
    """Cadena LCEL: prompt -> LLM con salida estructurada (RoutingDecision)."""
    prompt = ChatPromptTemplate.from_messages(
        [("system", ORCHESTRATOR_SYSTEM_PROMPT), ("human", "Consulta del usuario: {question}")]
    )
    return (prompt | llm.with_structured_output(RoutingDecision)).with_config(run_name="orchestrator-routing")
