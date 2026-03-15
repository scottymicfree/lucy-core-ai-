from typing import Dict, Any
import logging

from utils.config_loader import ConfigLoader
from utils.event_bus import EventBus

# Import all agents
from agents.performance.perfmon import PerfMonAgent
from agents.storage.datavault import DataVaultAgent
from agents.task_workflow.taskflow import TaskFlowAgent
from agents.safety.safeguard import SafeGuardAgent
from agents.interaction.interact_ui import InteractUIAgent
from agents.reasoning.thinktank import ThinkTankAgent
from agents.human_context.humana import HumanaAgent
from agents.self_reflection.introspect import IntrospectAgent
from agents.dashboard.vizdash import VizDashAgent
from agents.learning_update.evolve_core import EvolveCoreAgent

from agents.base_agent import BaseAgent

logging.basicConfig(level=logging.INFO, format='[%(levelname)s] %(message)s')

class LucyOrchestrator:
    def __init__(self) -> None:
        self.config_loader = ConfigLoader()
        self.event_bus = EventBus()
        self.config: Dict[str, Any] = {}
        self.agents: Dict[str, BaseAgent] = {}

    def initialize(self) -> None:
        logging.info("Initializing Lucy Orchestrator...")

        # Load configuration
        try:
            self.config = self.config_loader.load_yaml("system_config.yaml")
        except FileNotFoundError:
            logging.warning("No system_config.yaml found, using defaults.")

        # Instantiate agents
        self.agents = {
            "perfmon": PerfMonAgent(),
            "datavault": DataVaultAgent(),
            "taskflow": TaskFlowAgent(),
            "safeguard": SafeGuardAgent(),
            "interact_ui": InteractUIAgent(),
            "thinktank": ThinkTankAgent(),
            "humana": HumanaAgent(),
            "introspect": IntrospectAgent(),
            "vizdash": VizDashAgent(),
            "evolvecore": EvolveCoreAgent()
        }

        # Start all agents
        for name, agent in self.agents.items():
            agent.start()
            logging.info(f"{name} started successfully.")

        logging.info("Lucy Orchestrator initialized with all agents.")

    def shutdown(self) -> None:
        logging.info("Shutting down Lucy Orchestrator...")
        for name, agent in self.agents.items():
            agent.stop()
            logging.info(f"{name} stopped.")
        logging.info("Shutdown complete.")

    def health_report(self) -> Dict[str, Any]:
        report = {}
        for name, agent in self.agents.items():
            report[name] = agent.health_check()
        return report

    def run(self) -> None:
        logging.info("Lucy is now running...")
        report = self.health_report()
        for name, status in report.items():
            logging.info(f"{name}: {status}")
