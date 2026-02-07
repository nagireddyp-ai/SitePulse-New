from fastapi import APIRouter

router = APIRouter()


@router.post("/")
def chat() -> dict:
    return {"message": "chat endpoint scaffold"}
