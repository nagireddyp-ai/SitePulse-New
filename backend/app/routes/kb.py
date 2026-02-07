from fastapi import APIRouter

from app.services.rag_service import RagService

router = APIRouter()
rag_service = RagService()


@router.get("/")
def list_articles() -> dict:
    return {"items": rag_service.list_documents(), "source": "chroma"}
