"""Console interface for the Student Task Manager."""

from task_manager import TaskManager

DATA_FILE = "tasks.json"

MENU = """
==== Student Task Manager ====
1. Add task
2. Show tasks
3. Complete task
4. Delete task
5. Exit"""


def read_task_id(prompt="Enter task ID: "):
    """Ask for a task id and return it as an int, or None if it is not a number."""
    value = input(prompt).strip()
    if not value.isdigit():
        print("Please enter a valid numeric task ID.")
        return None
    return int(value)


def handle_add(manager):
    title = input("Task title: ")
    try:
        task = manager.add_task(title)
    except ValueError as error:
        print(f"Error: {error}")
        return
    print(f"Added task #{task.id}: {task.title}")


def handle_list(manager):
    tasks = manager.list_tasks()
    if not tasks:
        print("No tasks yet.")
        return
    for task in tasks:
        status = "x" if task.completed else " "
        print(f"[{status}] {task.id}. {task.title}")


def handle_complete(manager):
    print("Completing tasks is not available yet.")


def handle_delete(manager):
    print("Deleting tasks is not available yet.")


def main():
    manager = TaskManager(DATA_FILE)
    actions = {
        "1": handle_add,
        "2": handle_list,
        "3": handle_complete,
        "4": handle_delete,
    }
    while True:
        print(MENU)
        try:
            choice = input("Choose an option: ").strip()
        except (EOFError, KeyboardInterrupt):
            print()
            choice = "5"
        if choice == "5":
            print("Goodbye!")
            break
        action = actions.get(choice)
        if action is None:
            print("Invalid option, please choose 1-5.")
            continue
        action(manager)


if __name__ == "__main__":
    main()
