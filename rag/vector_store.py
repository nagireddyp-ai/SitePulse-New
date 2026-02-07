from typing import Any

import chromadb


class VectorStore:
    def __init__(self, path: str, collection_name: str = "sitepulse") -> None:
        client = chromadb.PersistentClient(path=path)
        self.collection = client.get_or_create_collection(name=collection_name)

    def add_documents(self, ids: list[str], embeddings: list[list[float]], documents: list[str], metadatas: list[dict[str, Any]]) -> None:
        self.collection.add(
            ids=ids,
            embeddings=embeddings,
            documents=documents,
            metadatas=metadatas,
        )

    def query(self, query_embeddings: list[list[float]], n_results: int, where: dict[str, Any] | None = None) -> dict[str, Any]:
        return self.collection.query(
            query_embeddings=query_embeddings,
            n_results=n_results,
            where=where,
        )

    def list_documents(self, limit: int = 50) -> dict[str, Any]:
        return self.collection.get(limit=limit)
