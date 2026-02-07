from pydantic import BaseModel


class Metrics(BaseModel):
    mttr_minutes: float
    sla_breaches: int
    ticket_volume: int
    agent_actions: int
