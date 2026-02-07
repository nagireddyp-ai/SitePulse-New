from fastapi import APIRouter

router = APIRouter()


@router.get("/")
def metrics() -> dict:
    return {
        "mttr_minutes": 0,
        "sla_breaches": 0,
        "ticket_volume": 0,
    }
