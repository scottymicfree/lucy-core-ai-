from abc import ABC, abstractmethod
from typing import Any, Dict
import logging

logging.basicConfig(level=logging.INFO, format='[%(levelname)s] %(message)s')

class BaseAgent(ABC):
    def __init__(self, name: str) -> None:
        self.name = name
        self.status = "idle"

    @abstractmethod
    def start(self) -> None:
        self.status = "running"
        logging.info(f"{self.name} started.")

    @abstractmethod
    def stop(self) -> None:
        self.status = "stopped"
        logging.info(f"{self.name} stopped.")

    @abstractmethod
    def health_check(self) -> Dict[str, Any]:
        return {"agent": self.name, "status": self.status}
