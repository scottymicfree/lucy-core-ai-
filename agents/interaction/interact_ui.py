# InteractUI agent ffrom typing import Dict, Any
from agents.base_agent import BaseAgent

class InteractUIAgent(BaseAgent):
    def __init__(self) -> None:
        super().__init__("InteractUI")
        self.input_buffer = []
        self.output_buffer = []

    def start(self) -> None:
        self.status = "running"

    def stop(self) -> None:
        self.status = "stopped"

    def receive_input(self, user_input: str) -> None:
        """Receive user input for processing."""
        self.input_buffer.append(user_input)

    def send_output(self, message: str) -> None:
        """Store message to be displayed to user."""
        self.output_buffer.append(message)
        print(f"Lucy: {message}")

    def get_latest_input(self) -> str:
        """Return the latest user input."""
        if self.input_buffer:
            return self.input_buffer.pop(0)
        return ""

    def health_check(self) -> Dict[str, Any]:
        return {
            "agent": self.name,
            "status": self.status,
            "input_buffer_length": len(self.input_buffer),
            "output_buffer_length": len(self.output_buffer)
        }or CLI input/output
