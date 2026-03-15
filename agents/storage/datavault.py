from typing import Dict, Any
import json
from agents.base_agent import BaseAgent
from pathlib import Path

class DataVaultAgent(BaseAgent):
    def __init__(self, storage_dir: str = "data/state") -> None:
        super().__init__("DataVault")
        self.storage_dir = Path(storage_dir)
        self.storage_dir.mkdir(parents=True, exist_ok=True)

    def start(self) -> None:
        self.status = "running"

    def stop(self) -> None:
        self.status = "stopped"

    def save_state(self, filename: str, data: Dict[str, Any]) -> None:
        file_path = self.storage_dir / filename
        with file_path.open("w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)

    def load_state(self, filename: str) -> Dict[str, Any]:
        file_path = self.storage_dir / filename
        if not file_path.exists():
            return {}
        with file_path.open("r", encoding="utf-8") as f:
            return json.load(f)

    def health_check(self) -> Dict[str, object]:
        return {
            "agent": self.name,
            "status": self.status,
            "storage_path_exists": self.storage_dir.exists()
        }
