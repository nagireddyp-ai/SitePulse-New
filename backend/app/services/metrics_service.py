from dataclasses import dataclass


@dataclass
class MetricsState:
    mttr_minutes: float = 0.0
    sla_breaches: int = 0
    ticket_volume: int = 0
    agent_actions: int = 0


class MetricsService:
    def __init__(self) -> None:
        self.state = MetricsState()

    def record_incident(self) -> None:
        self.state.ticket_volume += 1

    def record_sla_breach(self) -> None:
        self.state.sla_breaches += 1

    def record_agent_action(self) -> None:
        self.state.agent_actions += 1

    def update_mttr(self, mttr_minutes: float) -> None:
        self.state.mttr_minutes = mttr_minutes

    def snapshot(self) -> MetricsState:
        return self.state


metrics_service = MetricsService()
