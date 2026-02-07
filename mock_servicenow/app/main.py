from pathlib import Path

from fastapi import FastAPI, HTTPException

from mock_servicenow.app.services.storage import MockStorage

app = FastAPI(title="Mock ServiceNow", version="0.1.0")

storage = MockStorage(Path(__file__).resolve().parents[2] / "data")


@app.get("/incidents")
def list_incidents() -> dict:
    items = [incident.dict() for incident in storage.list_incidents()]
    return {"items": items}


@app.post("/incidents/update")
def update_incident(payload: dict) -> dict:
    incident_id = payload.get("incident_id")
    status = payload.get("status")
    resolution = payload.get("resolution")
    if not incident_id or not status:
        raise HTTPException(status_code=400, detail="incident_id and status required")
    incident = storage.update_incident(incident_id, status, resolution)
    if not incident:
        raise HTTPException(status_code=404, detail="incident not found")
    return incident.dict()


@app.get("/service-requests")
def list_service_requests() -> dict:
    items = [request.dict() for request in storage.list_service_requests()]
    return {"items": items}


@app.post("/service-requests/resolve")
def resolve_service_request(payload: dict) -> dict:
    request_id = payload.get("request_id")
    resolution = payload.get("resolution")
    if not request_id or not resolution:
        raise HTTPException(status_code=400, detail="request_id and resolution required")
    request = storage.resolve_service_request(request_id, resolution)
    if not request:
        raise HTTPException(status_code=404, detail="request not found")
    return request.dict()
