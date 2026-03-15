from typing import Dict, Any
from agents.base_agent import BaseAgent

class VizDashAgent(BaseAgent):
    def __init__(self) -> None:
        super().__init__("VizDash")
        self.telemetry_data = {}

    def start(self) -> None:
        self.status = "running"

    def stop(self) -> None:
        self.status = "stopped"

    def update_telemetry(self, agent_name: str, data: Dict[str, Any]) -> None:
        """Update telemetry data for a given agent."""
        self.telemetry_data[agent_name] = data

    def display_dashboard(self) -> None:
        """Simulate dashboard output."""
        print("=== Lucy Dashboard ===")
        for agent, data in self.telemetry_data.items():
            print(f"{agent}: {data}")
        print("=====================")

    def health_check(self) -> Dict[str, Any]:
        return {
            "agent": self.name,
            "status": self.status,
            "tracked_agents": list(self.telemetry_data.keys())
        }
