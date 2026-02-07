from dataclasses import dataclass


@dataclass
class EmbeddingResult:
    vector: list[float]
    text: str
