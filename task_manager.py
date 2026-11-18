"""Core logic for the Student Task Manager."""

import json
import os
from dataclasses import asdict, dataclass


@dataclass
class Task:
    """A single to-do item."""

    id: int
    title: str
    completed: bool = False


class TaskManager:
    """Keeps the list of tasks and saves them to a JSON file if a path is given."""

    def __init__(self, storage_path=None):
        self.storage_path = storage_path
        self.tasks = []
        if storage_path:
            self.load()

    def _next_id(self):
        return max((task.id for task in self.tasks), default=0) + 1

    # ----- add -----

    def add_task(self, title):
        """Create a new task and return it."""
        task = Task(id=self._next_id(), title=title)
        self.tasks.append(task)
        self.save()
        return task

    # ----- display -----

    def list_tasks(self):
        """Return all tasks in the order they were added."""
        return list(self.tasks)

    def get_task(self, task_id):
        """Return the task with the given id, or None if it does not exist."""
        for task in self.tasks:
            if task.id == task_id:
                return task
        return None

    # ----- complete -----

    def complete_task(self, task_id):
        """Mark a task as completed."""
        raise NotImplementedError("Completing tasks is not implemented yet")

    # ----- delete -----

    def delete_task(self, task_id):
        """Remove the task with the given id and return it.

        Raises ValueError if no task has that id.
        """
        task = self.get_task(task_id)
        if task is None:
            raise ValueError(f"No task found with ID {task_id}.")
        self.tasks.remove(task)
        self.save()
        return task

    # ----- persistence -----

    def save(self):
        """Write all tasks to the JSON file (does nothing without a storage path)."""
        if not self.storage_path:
            return
        with open(self.storage_path, "w", encoding="utf-8") as file:
            json.dump([asdict(task) for task in self.tasks], file, indent=2)

    def load(self):
        """Read tasks from the JSON file if it exists."""
        if not self.storage_path or not os.path.exists(self.storage_path):
            return
        with open(self.storage_path, encoding="utf-8") as file:
            self.tasks = [Task(**item) for item in json.load(file)]
