from collections import Counter
from typing import Any


def keyword_score(query: str, text: str) -> float:
    query_tokens = [token.lower() for token in query.split()]
    text_tokens = [token.lower() for token in text.split()]
    query_counts = Counter(query_tokens)
    text_counts = Counter(text_tokens)
    overlap = sum((query_counts & text_counts).values())
    return overlap / max(len(query_tokens), 1)


def merge_results(vector_results: dict[str, Any], query: str, top_k: int) -> list[dict[str, Any]]:
    documents = vector_results.get("documents", [[]])[0]
    metadatas = vector_results.get("metadatas", [[]])[0]
    ids = vector_results.get("ids", [[]])[0]
    distances = vector_results.get("distances", [[]])[0]

    combined: list[dict[str, Any]] = []
    for doc, metadata, doc_id, distance in zip(documents, metadatas, ids, distances):
        score = keyword_score(query, doc)
        combined.append(
            {
                "id": doc_id,
                "document": doc,
                "metadata": metadata,
                "vector_distance": distance,
                "keyword_score": score,
            }
        )

    combined.sort(key=lambda item: (item["vector_distance"], -item["keyword_score"]))
    return combined[:top_k]
