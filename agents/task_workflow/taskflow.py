from typing import Dict, Any, List, Callable
from agents.base_agent import BaseAgent

class TaskFlowAgent(BaseAgent):
    def __init__(self) -> None:
        super().__init__("TaskFlow")
        self.tasks: List[Dict[str, Any]] = []

    def start(self) -> None:
        self.status = "running"

    def stop(self) -> None:
        self.status = "stopped"

    def add_task(self, task_name: str, action: Callable[..., Any], *args, **kwargs) -> None:
        """Add a new task to the workflow queue."""
        self.tasks.append({
            "name": task_name,
            "action": action,
            "args": args,
            "kwargs": kwargs,
            "status": "pending"
        })

    def execute_next(self) -> None:
        """Execute the next pending task in the queue."""
        for task in self.tasks:
            if task["status"] == "pending":
                try:
                    task["action"](*task["args"], **task["kwargs"])
                    task["status"] = "completed"
                except Exception as e:
                    task["status"] = f"error: {e}"
                break  # execute one task at a time

    def execute_all(self) -> None:
        """Run all pending tasks in order."""
        for task in self.tasks:
            if task["status"] == "pending":
                try:
                    task["action"](*task["args"], **task["kwargs"])
                    task["status"] = "completed"
                except Exception as e:
                    task["status"] = f"error: {e}"

    def health_check(self) -> Dict[str, Any]:
        return {
            "agent": self.name,
            "status": self.status,
            "total_tasks": len(self.tasks),
            "pending_tasks": sum(1 for t in self.tasks if t["status"] == "pending")
        }
