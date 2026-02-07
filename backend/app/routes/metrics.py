from fastapi import APIRouter

from app.services.metrics_service import metrics_service

router = APIRouter()


@router.get("/")
def metrics() -> dict:
    snapshot = metrics_service.snapshot()
    return snapshot.__dict__
