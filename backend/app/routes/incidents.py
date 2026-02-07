from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def list_incidents() -> dict:
    return {"items": [], "source": "mock"}
