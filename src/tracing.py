"""
tracing.py — Integración con Langfuse (observability).

Un único punto de entrada para el resto del sistema:
  * langfuse_enabled()  -> True si hay claves de Langfuse configuradas
  * get_langfuse()      -> cliente de Langfuse (o None)
  * traced_run(...)     -> context manager que abre la traza raíz de UNA consulta y
                           entrega (callback_handler, trace_id) para que todo lo que
                           ocurra adentro (orquestador, retrievers, agentes, LLM calls,
                           evaluador) quede anidado en la MISMA traza.
  * flush()             -> fuerza el envío de eventos pendientes

Si faltan las claves, el sistema sigue funcionando SIN trazas (con un aviso), así el
repo es ejecutable aunque quien lo corra no tenga cuenta de Langfuse.
Requiere el SDK de Langfuse v4 (get_client, start_as_current_observation, propagate_attributes).
"""

import os
from contextlib import contextmanager
from typing import Any, Iterator, List, Optional, Tuple

from src import config  # noqa: F401  (carga .env)


def langfuse_enabled() -> bool:
    pk = os.getenv("LANGFUSE_PUBLIC_KEY", "")
    sk = os.getenv("LANGFUSE_SECRET_KEY", "")
    return pk.startswith("pk-lf-") and sk.startswith("sk-lf-") and "xxx" not in pk + sk


def _normalize_host_env() -> None:
    """El SDK v4 usa LANGFUSE_BASE_URL; aceptamos también LANGFUSE_HOST (nombre histórico)."""
    host = os.getenv("LANGFUSE_HOST")
    if host and not os.getenv("LANGFUSE_BASE_URL"):
        os.environ["LANGFUSE_BASE_URL"] = host


def get_langfuse() -> Optional[Any]:
    """Cliente singleton de Langfuse o None si no está configurado."""
    if not langfuse_enabled():
        return None
    _normalize_host_env()
    from langfuse import get_client

    return get_client()


@contextmanager
def traced_run(
    name: str,
    input_data: Any,
    session_id: Optional[str] = None,
    user_id: Optional[str] = None,
    tags: Optional[List[str]] = None,
) -> Iterator[Tuple[Optional[Any], Optional[str], Any]]:
    """
    Abre la traza raíz de una consulta.

    Devuelve (handler, trace_id, root_span):
      - handler: CallbackHandler de LangChain para pasar en config={"callbacks": [handler]}
      - trace_id: id de la traza (se usa para colgar los scores del evaluador)
      - root_span: span raíz, para actualizar su output al final (None si no hay Langfuse)
    """
    client = get_langfuse()
    if client is None:
        yield None, None, None
        return

    from langfuse import propagate_attributes
    from langfuse.langchain import CallbackHandler

    with client.start_as_current_observation(name=name, as_type="agent", input=input_data) as root:
        with propagate_attributes(
            session_id=session_id, user_id=user_id, tags=tags or [], trace_name=name
        ):
            handler = CallbackHandler()
            yield handler, client.get_current_trace_id(), root


@contextmanager
def trace_attributes(tags: Optional[List[str]] = None, metadata: Optional[dict] = None) -> Iterator[None]:
    """
    Agrega tags y metadata (strings) a todo lo que se ejecute adentro: así en Langfuse se puede
    filtrar por área elegida (tag `dept:HR`), por casos `misclassified` y comparar
    `expected_intent` vs `actual_intent` abriendo la traza. No-op si Langfuse no está activo.
    """
    if not langfuse_enabled():
        yield
        return

    from langfuse import propagate_attributes

    clean_meta = {k: str(v)[:200] for k, v in (metadata or {}).items()}
    with propagate_attributes(tags=tags or [], metadata=clean_meta):
        yield


def flush() -> None:
    """Envía los eventos pendientes (imprescindible en scripts cortos y notebooks)."""
    client = get_langfuse()
    if client is not None:
        client.flush()
