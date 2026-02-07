from agents.sitepulse_agents.agents import (
    IncidentTriageAgent,
    ITSMSyncAgent,
    KnowledgeGenerationAgent,
    MonitoringAgent,
)
from agents.sitepulse_agents.contracts import Incident
from app.services.metrics_service import metrics_service
from app.services.rag_service import RagService
from app.services.servicenow_client import ServiceNowClient


class AgentService:
    def __init__(self) -> None:
        self.triage_agent = IncidentTriageAgent()
        self.kb_agent = KnowledgeGenerationAgent()
        self.itsm_agent = ITSMSyncAgent()
        self.monitor_agent = MonitoringAgent()
        self.rag_service = RagService()
        self.servicenow_client = ServiceNowClient()

    def process_incident(self, incident_payload: dict) -> dict:
        incident = Incident(**incident_payload)
        triage = self.triage_agent.triage(incident)
        kb_article = self.kb_agent.generate_article(incident, triage.suggested_resolution)
        self.rag_service.ingest_document(
            kb_article.body,
            metadata={
                "type": "kb",
                "title": kb_article.title,
                "incident_id": incident.incident_id,
            },
        )
        metrics_service.record_agent_action()
        sla_breach = self.monitor_agent.evaluate_sla(incident)
        if sla_breach:
            metrics_service.record_sla_breach()
        update_payload = self.itsm_agent.prepare_update(
            incident,
            status="In Progress",
            resolution=triage.suggested_resolution,
        )
        update_result = self.servicenow_client.update_incident(update_payload)
        return {
            "triage": triage.__dict__,
            "kb_article": kb_article.__dict__,
            "itsm_update": update_result,
            "sla_breach": sla_breach,
        }


agent_service = AgentService()
