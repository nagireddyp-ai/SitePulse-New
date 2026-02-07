from dataclasses import dataclass


@dataclass
class Chunk:
    text: str
    metadata: dict


def chunk_text(text: str, chunk_size: int = 512, overlap: int = 100) -> list[Chunk]:
    tokens = text.split()
    chunks: list[Chunk] = []
    start = 0
    index = 0

    while start < len(tokens):
        end = min(start + chunk_size, len(tokens))
        chunk_tokens = tokens[start:end]
        chunk_text_value = " ".join(chunk_tokens)
        chunks.append(
            Chunk(
                text=chunk_text_value,
                metadata={
                    "chunk_index": index,
                    "token_start": start,
                    "token_end": end,
                },
            )
        )
        index += 1
        start = end - overlap
        if start < 0:
            start = 0
        if start >= len(tokens):
            break

    return chunks
