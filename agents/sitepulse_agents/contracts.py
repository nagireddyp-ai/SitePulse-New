from dataclasses import dataclass


@dataclass
class Incident:
    incident_id: str
    title: str
    description: str
    priority: str
    status: str
    sla_minutes_remaining: int


@dataclass
class KnowledgeArticle:
    article_id: str
    title: str
    body: str
    tags: list[str]
    sources: list[str]
