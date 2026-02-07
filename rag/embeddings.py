from typing import Iterable

import ollama

from rag.pipeline_types import EmbeddingResult


def embed_texts(texts: Iterable[str], model: str, host: str) -> list[EmbeddingResult]:
    results: list[EmbeddingResult] = []
    for text in texts:
        response = ollama.embeddings(model=model, prompt=text, host=host)
        results.append(EmbeddingResult(vector=response["embedding"], text=text))
    return results
