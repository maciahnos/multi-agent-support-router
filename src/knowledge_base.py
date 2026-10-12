"""
knowledge_base.py — Carga de documentos y construcción de vector stores por dominio.

Cada dominio (HR / TECH / FINANCE) tiene su propia carpeta en data/ y su propia
colección en Chroma. Así cada agente especializado sólo "ve" su base de
conocimiento, que es la idea central de los sistemas multiagente (L3).
"""

from pathlib import Path
from typing import Dict, List

from langchain_chroma import Chroma
from langchain_core.documents import Document
from langchain_openai import OpenAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter

from src import config

SUPPORTED_EXTENSIONS = {".md", ".txt"}


def load_domain_documents(domain: str) -> List[Document]:
    """Lee todos los .md/.txt de la carpeta del dominio como Documents con metadata."""
    folder = config.DATA_DIR / config.DOMAIN_FOLDERS[domain]
    if not folder.exists():
        raise FileNotFoundError(f"No existe la carpeta de documentos: {folder}")
    docs = []
    for path in sorted(folder.iterdir()):
        if path.suffix.lower() in SUPPORTED_EXTENSIONS:
            text = path.read_text(encoding="utf-8")
            docs.append(Document(page_content=text, metadata={"source": path.name, "domain": domain}))
    return docs


def split_documents(docs: List[Document]) -> List[Document]:
    """Divide los documentos en chunks con solapamiento, respetando títulos/párrafos."""
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=config.CHUNK_SIZE,
        chunk_overlap=config.CHUNK_OVERLAP,
        separators=["\n## ", "\n# ", "\n\n", "\n", ". ", " "],
    )
    chunks = splitter.split_documents(docs)
    for i, chunk in enumerate(chunks):
        chunk.metadata["chunk_id"] = i
    return chunks


def build_vector_store(domain: str, embeddings: OpenAIEmbeddings, rebuild: bool = False) -> Chroma:
    """Crea (o reutiliza) la colección Chroma persistida del dominio."""
    persist_dir = str(config.VECTOR_DIR / domain.lower())
    store = Chroma(
        collection_name=f"nimbus_{domain.lower()}",
        embedding_function=embeddings,
        persist_directory=persist_dir,
    )
    if rebuild:
        store.reset_collection()
    if store._collection.count() == 0:
        chunks = split_documents(load_domain_documents(domain))
        if len(chunks) < config.MIN_CHUNKS_PER_DOMAIN:
            raise ValueError(
                f"El dominio {domain} tiene {len(chunks)} chunks (< {config.MIN_CHUNKS_PER_DOMAIN})."
            )
        store.add_documents(chunks)
    return store


def build_all_vector_stores(rebuild: bool = False) -> Dict[str, Chroma]:
    """Devuelve {dominio: vector_store} para HR, TECH y FINANCE."""
    embeddings = OpenAIEmbeddings(model=config.EMBEDDING_MODEL, api_key=config.require_openai_key())
    return {domain: build_vector_store(domain, embeddings, rebuild) for domain in config.DOMAIN_FOLDERS}


def count_chunks_per_domain() -> Dict[str, int]:
    """Cuenta chunks por dominio SIN llamar a la API (sirve para verificar el mínimo de 50)."""
    return {d: len(split_documents(load_domain_documents(d))) for d in config.DOMAIN_FOLDERS}
