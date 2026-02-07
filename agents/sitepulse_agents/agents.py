from dataclasses import dataclass

from agents.sitepulse_agents.contracts import Incident, KnowledgeArticle


@dataclass
class TriageResult:
    severity: str
    suggested_resolution: str


class IncidentTriageAgent:
    def triage(self, incident: Incident) -> TriageResult:
        severity = "high" if incident.priority in {"P1", "P2"} else "medium"
        resolution = (
            f"Investigate {incident.title}. "
            "Check system logs, validate recent changes, and apply standard remediation steps."
        )
        return TriageResult(severity=severity, suggested_resolution=resolution)


class KnowledgeGenerationAgent:
    def generate_article(self, incident: Incident, resolution: str) -> KnowledgeArticle:
        return KnowledgeArticle(
            article_id=f"KB-{incident.incident_id}",
            title=f"Resolution for {incident.title}",
            body=(
                f"Incident: {incident.description}\n\n"
                f"Resolution Steps: {resolution}\n\n"
                "Validation: Confirm service health and monitor logs."
            ),
            tags=["linux", incident.priority, incident.status],
            sources=[incident.incident_id],
        )


class RealtimeRagChatAgent:
    def build_response(self, question: str, sources: list[dict]) -> str:
        source_titles = ", ".join(item["metadata"].get("title", "source") for item in sources)
        return f"Based on {source_titles}, here is the guidance: {question}"


class ITSMSyncAgent:
    def prepare_update(self, incident: Incident, status: str, resolution: str) -> dict:
        return {
            "incident_id": incident.incident_id,
            "status": status,
            "resolution": resolution,
        }


class MonitoringAgent:
    def evaluate_sla(self, incident: Incident) -> bool:
        return incident.sla_minutes_remaining <= 0
