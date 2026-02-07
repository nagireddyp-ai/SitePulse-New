from pydantic import BaseModel


class ServiceRequest(BaseModel):
    request_id: str
    title: str
    description: str
    priority: str
    status: str
    assigned_group: str
    resolution: str | None = None
