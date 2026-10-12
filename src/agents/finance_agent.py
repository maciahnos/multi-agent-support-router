"""finance_agent.py — Agente RAG de Finanzas."""

from langchain_chroma import Chroma
from langchain_openai import ChatOpenAI

from src.agents.rag_agent import RAGAgent


def create_finance_agent(vector_store: Chroma, llm: ChatOpenAI) -> RAGAgent:
    return RAGAgent(
        name="finance-agent",
        domain="FINANCE",
        role="el Analista de Finanzas de Nimbus Cloud (gastos, reembolsos, facturación, compras, presupuesto, pagos)",
        contact="finanzas@nimbuscloud.example",
        vector_store=vector_store,
        llm=llm,
    )
