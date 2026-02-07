import json
from pathlib import Path

from mock_servicenow.app.models.incident import Incident
from mock_servicenow.app.models.service_request import ServiceRequest


class MockStorage:
    def __init__(self, data_path: Path) -> None:
        self.data_path = data_path
        self._incidents = self._load("incidents.json", Incident)
        self._service_requests = self._load("service_requests.json", ServiceRequest)

    def _load(self, filename: str, model):
        file_path = self.data_path / filename
        data = json.loads(file_path.read_text())
        return [model(**item) for item in data]

    def list_incidents(self) -> list[Incident]:
        return self._incidents

    def update_incident(self, incident_id: str, status: str, resolution: str | None = None) -> Incident | None:
        for incident in self._incidents:
            if incident.incident_id == incident_id:
                incident.status = status
                if resolution:
                    incident.resolution = resolution
                return incident
        return None

    def list_service_requests(self) -> list[ServiceRequest]:
        return self._service_requests

    def resolve_service_request(self, request_id: str, resolution: str) -> ServiceRequest | None:
        for request in self._service_requests:
            if request.request_id == request_id:
                request.status = "Resolved"
                request.resolution = resolution
                return request
        return None
