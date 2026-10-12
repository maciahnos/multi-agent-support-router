"""tech_agent.py — Agente RAG de Soporte Técnico / IT."""

from langchain_chroma import Chroma
from langchain_openai import ChatOpenAI

from src.agents.rag_agent import RAGAgent


def create_tech_agent(vector_store: Chroma, llm: ChatOpenAI) -> RAGAgent:
    return RAGAgent(
        name="tech-agent",
        domain="TECH",
        role="el Solucionador de Soporte Técnico de Nimbus Cloud (cuentas, accesos, VPN, equipamiento, software, tickets)",
        contact="it-help@nimbuscloud.example",
        vector_store=vector_store,
        llm=llm,
    )
