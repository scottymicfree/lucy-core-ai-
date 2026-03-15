from typing import Dict
import psutil
from agents.base_agent import BaseAgent

class PerfMonAgent(BaseAgent):
    def __init__(self) -> None:
        super().__init__("PerfMon")

    def start(self) -> None:
        self.status = "running"

    def stop(self) -> None:
        self.status = "stopped"

    def health_check(self) -> Dict[str, object]:
        return {
            "agent": self.name,
            "status": self.status,
            "cpu_percent": psutil.cpu_percent(interval=0.1),
            "memory_percent": psutil.virtual_memory().percent,
            "disk_percent": psutil.disk_usage("/").percent,
        }
