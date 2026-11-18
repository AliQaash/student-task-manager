# User Guide: Student Task Manager

## Starting the program

Open a terminal in the project folder and run:

```bash
python3 main.py
```

The main menu appears:

```
==== Student Task Manager ====
1. Add task
2. Show tasks
3. Complete task
4. Delete task
5. Exit
```

Type the number of an option and press **Enter**.

## 1. Add a task

Choose `1` and type the task title.

```
Task title: Prepare for DevOps viva
Added task #1: Prepare for DevOps viva
```

An empty title (or one made only of spaces) is not accepted:

```
Task title:
Error: Task title cannot be empty.
```

## 2. Show tasks

Choose `2` to see every task. `[x]` means completed and `[ ]` means still pending.

```
[ ] 1. Prepare for DevOps viva
[x] 2. Submit lab report
```

## 3. Complete a task

Choose `3`. The task list is shown; type the ID of the task you finished.

```
Enter the ID of the task to complete: 1
Task #1 marked as completed.
```

## 4. Delete a task

Choose `4` and type the ID of the task to remove.

```
Enter the ID of the task to delete: 2
Deleted task #2: Submit lab report
```

If the ID is not a number, or no task has that ID, an error message is shown and nothing
is deleted.

## 5. Exit

Choose `5` to quit. Your tasks are saved in `tasks.json` and will be there next time you
start the program. Delete that file if you want to start with an empty list.
