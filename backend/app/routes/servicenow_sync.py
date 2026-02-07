from fastapi import APIRouter

from app.services.agent_service import agent_service
from app.services.servicenow_client import ServiceNowClient

router = APIRouter()
servicenow_client = ServiceNowClient()


@router.post("/")
def sync_servicenow() -> dict:
    incidents = servicenow_client.list_incidents()
    processed = [agent_service.process_incident(incident) for incident in incidents]
    return {"status": "completed", "processed": processed}
