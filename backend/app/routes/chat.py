from fastapi import APIRouter

from app.models.chat import ChatRequest, ChatResponse
from app.services.rag_service import RagService

router = APIRouter()
rag_service = RagService()


@router.post("/", response_model=ChatResponse)
def chat(payload: ChatRequest) -> ChatResponse:
    result = rag_service.answer(payload.question, top_k=payload.top_k, filters=payload.context)
    return ChatResponse(answer=result["answer"], sources=result["sources"])
