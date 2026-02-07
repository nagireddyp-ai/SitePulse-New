from pydantic import BaseModel


class ChatRequest(BaseModel):
    question: str
    context: dict | None = None
    top_k: int = 4


class ChatResponse(BaseModel):
    answer: str
    sources: list[dict]
