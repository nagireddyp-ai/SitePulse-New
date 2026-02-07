import uuid
from typing import Any

from rag.chunking import chunk_text
from rag.embeddings import embed_texts
from rag.retriever import merge_results
from rag.vector_store import VectorStore


class RagPipeline:
    def __init__(self, chroma_path: str, model: str, embedding_model: str, ollama_host: str) -> None:
        self.store = VectorStore(path=chroma_path)
        self.model = model
        self.embedding_model = embedding_model
        self.ollama_host = ollama_host

    def ingest(self, text: str, metadata: dict[str, Any]) -> list[str]:
        chunks = chunk_text(text)
        chunk_texts = [chunk.text for chunk in chunks]
        embeddings = embed_texts(chunk_texts, model=self.embedding_model, host=self.ollama_host)
        ids = [str(uuid.uuid4()) for _ in chunks]
        metadatas = [
            {**metadata, **chunk.metadata}
            for chunk in chunks
        ]
        self.store.add_documents(
            ids=ids,
            embeddings=[item.vector for item in embeddings],
            documents=[item.text for item in embeddings],
            metadatas=metadatas,
        )
        return ids

    def retrieve(self, query: str, top_k: int = 4, filters: dict[str, Any] | None = None) -> list[dict[str, Any]]:
        query_embedding = embed_texts([query], model=self.embedding_model, host=self.ollama_host)[0]
        results = self.store.query(
            query_embeddings=[query_embedding.vector],
            n_results=top_k,
            where=filters,
        )
        return merge_results(results, query=query, top_k=top_k)

    def list_documents(self, limit: int = 50) -> dict[str, Any]:
        return self.store.list_documents(limit=limit)
