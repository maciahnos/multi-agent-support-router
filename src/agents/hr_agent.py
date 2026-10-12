"""hr_agent.py — Agente RAG de Recursos Humanos."""

from langchain_chroma import Chroma
from langchain_openai import ChatOpenAI

from src.agents.rag_agent import RAGAgent


def create_hr_agent(vector_store: Chroma, llm: ChatOpenAI) -> RAGAgent:
    return RAGAgent(
        name="hr-agent",
        domain="HR",
        role="el Especialista de RR.HH. de Nimbus Cloud (licencias, vacaciones, beneficios, desempeño, cultura)",
        contact="people@nimbuscloud.example",
        vector_store=vector_store,
        llm=llm,
    )
