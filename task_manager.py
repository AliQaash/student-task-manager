"""Core logic for the Student Task Manager."""

from dataclasses import dataclass


@dataclass
class Task:
    """A single to-do item."""

    id: int
    title: str
    completed: bool = False


class TaskManager:
    """Keeps the list of tasks in memory."""

    def __init__(self):
        self.tasks = []

    def _next_id(self):
        return max((task.id for task in self.tasks), default=0) + 1

    # ----- add -----

    def add_task(self, title):
        """Create a new task and return it."""
        task = Task(id=self._next_id(), title=title)
        self.tasks.append(task)
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
        """Delete a task."""
        raise NotImplementedError("Deleting tasks is not implemented yet")
