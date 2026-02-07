from fastapi import APIRouter

from app.services.agent_service import agent_service
from app.services.metrics_service import metrics_service
from app.services.servicenow_client import ServiceNowClient

router = APIRouter()
servicenow_client = ServiceNowClient()


@router.get("/")
def list_incidents() -> dict:
    items = servicenow_client.list_incidents()
    for _ in items:
        metrics_service.record_incident()
    return {"items": items, "source": "mock"}


@router.post("/process")
def process_incident(payload: dict) -> dict:
    return agent_service.process_incident(payload)
