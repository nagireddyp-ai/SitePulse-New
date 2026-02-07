from pydantic import BaseModel


class Incident(BaseModel):
    incident_id: str
    title: str
    description: str
    priority: str
    status: str
    sla_minutes_remaining: int
    assigned_group: str
    resolution: str | None = None
