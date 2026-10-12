"""
config.py — Configuración central del sistema multiagente.

Carga las variables de entorno desde .env (sin hardcodear secretos) y define
constantes compartidas: modelos, rutas, parámetros de chunking y de retrieval.
"""

import os
from pathlib import Path

from dotenv import load_dotenv

ROOT_DIR = Path(__file__).resolve().parent.parent
load_dotenv(ROOT_DIR / ".env")

# --- Modelos -----------------------------------------------------------------
CHAT_MODEL = os.getenv("CHAT_MODEL", "gpt-4o-mini")
EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL", "text-embedding-3-small")

# --- Rutas -------------------------------------------------------------------
DATA_DIR = ROOT_DIR / "data"
VECTOR_DIR = ROOT_DIR / ".vectorstores"          # persistencia de Chroma (se regenera)
TEST_QUERIES_PATH = ROOT_DIR / "test_queries.json"
OUTPUTS_DIR = ROOT_DIR / "outputs"

# --- Dominios: nombre canónico -> carpeta de documentos ----------------------
DOMAIN_FOLDERS = {
    "HR": "hr_docs",
    "TECH": "tech_docs",
    "FINANCE": "finance_docs",
}

# --- Chunking y retrieval ----------------------------------------------------
CHUNK_SIZE = 800        # caracteres (~150-200 tokens)
CHUNK_OVERLAP = 120     # ~15 % de solapamiento para no cortar ideas a la mitad
TOP_K = 4               # fragmentos recuperados por consulta
MIN_CHUNKS_PER_DOMAIN = 50   # requisito de la consigna


def require_openai_key() -> str:
    """Devuelve la API key de OpenAI o corta con un mensaje claro si falta."""
    key = os.getenv("OPENAI_API_KEY")
    if not key or key.startswith("your-key"):
        raise RuntimeError(
            "Falta OPENAI_API_KEY. Copiá .env.example a .env y completá tu clave real."
        )
    return key
