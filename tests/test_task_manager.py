"""Unit tests for the Student Task Manager."""

import os
import tempfile
import unittest

from task_manager import TaskManager


class TestAddTask(unittest.TestCase):
    def setUp(self):
        self.manager = TaskManager()

    def test_add_task_creates_pending_task(self):
        task = self.manager.add_task("Finish DevOps lab")
        self.assertEqual(task.id, 1)
        self.assertEqual(task.title, "Finish DevOps lab")
        self.assertFalse(task.completed)
        self.assertEqual(len(self.manager.list_tasks()), 1)

    def test_add_task_rejects_empty_title(self):
        with self.assertRaises(ValueError):
            self.manager.add_task("")
        with self.assertRaises(ValueError):
            self.manager.add_task("    ")
        self.assertEqual(self.manager.list_tasks(), [])

    def test_add_task_strips_whitespace(self):
        task = self.manager.add_task("  Read chapter 4  ")
        self.assertEqual(task.title, "Read chapter 4")


class TestCompleteTask(unittest.TestCase):
    def setUp(self):
        self.manager = TaskManager()
        self.task = self.manager.add_task("Submit assignment")

    def test_complete_task_marks_task_done(self):
        self.manager.complete_task(self.task.id)
        self.assertFalse(self.manager.get_task(self.task.id).completed)

    def test_complete_unknown_task_raises(self):
        with self.assertRaises(ValueError):
            self.manager.complete_task(99)


class TestDeleteTask(unittest.TestCase):
    def setUp(self):
        self.manager = TaskManager()
        self.first = self.manager.add_task("First")
        self.second = self.manager.add_task("Second")

    def test_delete_task_removes_only_that_task(self):
        self.manager.delete_task(self.first.id)
        remaining = self.manager.list_tasks()
        self.assertEqual(len(remaining), 1)
        self.assertEqual(remaining[0].title, "Second")

    def test_delete_unknown_task_raises(self):
        with self.assertRaises(ValueError):
            self.manager.delete_task(42)
        self.assertEqual(len(self.manager.list_tasks()), 2)


class TestPersistence(unittest.TestCase):
    def test_tasks_are_saved_and_loaded(self):
        with tempfile.TemporaryDirectory() as folder:
            path = os.path.join(folder, "tasks.json")
            manager = TaskManager(path)
            manager.add_task("Persist me")
            manager.complete_task(1)

            reloaded = TaskManager(path)
            self.assertEqual(len(reloaded.list_tasks()), 1)
            self.assertTrue(reloaded.get_task(1).completed)


if __name__ == "__main__":
    unittest.main()
