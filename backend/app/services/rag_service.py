from typing import Any

import ollama

from app.config.settings import settings
from rag.pipeline import RagPipeline


class RagService:
    def __init__(self) -> None:
        self.pipeline = RagPipeline(
            chroma_path=settings.chroma_path,
            model=settings.llm_model,
            embedding_model=settings.embedding_model,
            ollama_host=settings.ollama_host,
        )

    def answer(self, question: str, top_k: int = 4, filters: dict[str, Any] | None = None) -> dict[str, Any]:
        retrieved = self.pipeline.retrieve(question, top_k=top_k, filters=filters)
        context_blocks = [item["document"] for item in retrieved]
        context = "\n\n".join(context_blocks)
        prompt = (
            "You are SitePulse, an IT operations assistant. "
            "Answer the question using the context. "
            "If unsure, say you don't know.\n\n"
            f"Context:\n{context}\n\nQuestion: {question}\nAnswer:"
        )
        response = ollama.generate(model=settings.llm_model, prompt=prompt, host=settings.ollama_host)
        return {
            "answer": response["response"],
            "sources": retrieved,
        }

    def ingest_document(self, text: str, metadata: dict[str, Any]) -> list[str]:
        return self.pipeline.ingest(text, metadata)

    def list_documents(self, limit: int = 50) -> dict[str, Any]:
        return self.pipeline.list_documents(limit=limit)
