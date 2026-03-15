from typing import Any, Dict
from agents.base_agent import BaseAgent

class HumanaAgent(BaseAgent):
    def __init__(self) -> None:
        super().__init__("Humana")
        self.last_interaction = ""

    def start(self) -> None:
        self.status = "running"

    def stop(self) -> None:
        self.status = "stopped"

    def analyze_context(self, text: str) -> Dict[str, Any]:
        self.last_interaction = text
        # Lightweight context inference
        return {"urgency": "normal", "frustration": False}

    def health_check(self) -> Dict[str, Any]:
        return {"agent": self.name, "status": self.status}
