from typing import Any

import httpx

from app.config.settings import settings


class ServiceNowClient:
    def __init__(self, base_url: str | None = None) -> None:
        self.base_url = base_url or settings.servicenow_base_url

    def list_incidents(self) -> list[dict[str, Any]]:
        response = httpx.get(f"{self.base_url}/incidents", timeout=10)
        response.raise_for_status()
        return response.json().get("items", [])

    def update_incident(self, payload: dict[str, Any]) -> dict[str, Any]:
        response = httpx.post(f"{self.base_url}/incidents/update", json=payload, timeout=10)
        response.raise_for_status()
        return response.json()

    def list_service_requests(self) -> list[dict[str, Any]]:
        response = httpx.get(f"{self.base_url}/service-requests", timeout=10)
        response.raise_for_status()
        return response.json().get("items", [])

    def resolve_service_request(self, payload: dict[str, Any]) -> dict[str, Any]:
        response = httpx.post(
            f"{self.base_url}/service-requests/resolve",
            json=payload,
            timeout=10,
        )
        response.raise_for_status()
        return response.json()
