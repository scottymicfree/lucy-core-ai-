from typing import Dict

from utils.config_loader import ConfigLoader
from utils.event_bus import EventBus
from agents.performance.perfmon import PerfMonAgent
from agents.storage.datavault import DataVaultAgent
from agents.task_workflow.taskflow import TaskFlowAgent
from agents.safety.safeguard import SafeGuardAgent
from agents.interaction.interact_ui import InteractUIAgent


class LucyOrchestrator:
    def __init__(self) -> None:
        self.config_loader = ConfigLoader()
        self.event_bus = EventBus()
        self.config = {}
        self.agents: Dict[str, object] = {}

    def initialize(self) -> None:
        self.config = self.config_loader.load_yaml("system_config.yaml")

        self.agents["perfmon"] = PerfMonAgent()
        self.agents["datavault"] = DataVaultAgent()
        self.agents["taskflow"] = TaskFlowAgent()
        self.agents["safeguard"] = SafeGuardAgent()
        self.agents["interact_ui"] = InteractUIAgent()

        for agent in self.agents.values():
            agent.start()

        print("Lucy Orchestrator initialized successfully.")

    def run(self) -> None:
        print("Lucy is now running.")
        for name, agent in self.agents.items():
            print(f"{name}: {agent.health_check()}")
