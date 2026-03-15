from typing import Any, Dict
from agents.base_agent import BaseAgent

class IntrospectAgent(BaseAgent):
    def __init__(self) -> None:
        super().__init__("Introspect")
        self.last_check = ""

    def start(self) -> None:
        self.status = "running"

    def stop(self) -> None:
        self.status = "stopped"

    def evaluate(self, info: str) -> Dict[str, Any]:
        self.last_check = info
        return {"confidence": 0.95, "policy_compliant": True}

    def health_check(self) -> Dict[str, Any]:
        return {"agent": self.name, "status": self.status}
