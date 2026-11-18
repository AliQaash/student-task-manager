# Student Task Manager

![Tests](https://github.com/AliQaash/student-task-manager/actions/workflows/tests.yml/badge.svg)

A small Python console application that helps a student keep track of tasks.
It was built for CSC418 (DevOps for Cloud Computing) Lab Assignment 4 to practise a full
Git and GitHub workflow: commits, branches, Issues, Pull Requests, merge conflicts,
GitHub Actions and releases.

**Student:** Ali Qaash (FA23-BSE-026)

Project status: Released (v1.0.0)

## Features

- **Add tasks**: empty or whitespace-only titles are rejected, and titles are limited to 100 characters.
- **Show tasks**: every task is listed with its ID and a `[x]` / `[ ]` completion mark.
- **Complete tasks**: mark a task as done using its ID.
- **Delete tasks**: remove a task using a valid ID; unknown IDs show an error.
- **Saved between runs**: tasks are stored in `tasks.json`.
- **Automated tests**: `unittest` suite, run on GitHub Actions for every push and Pull Request to `main`.

## Requirements

- Python 3.8 or newer
- No third-party packages

## Setup

```bash
git clone https://github.com/AliQaash/student-task-manager.git
cd student-task-manager
```

## Usage

```bash
python3 main.py
```

```
==== Student Task Manager ====
1. Add task
2. Show tasks
3. Complete task
4. Delete task
5. Exit
Choose an option:
```

See [docs/user-guide.md](docs/user-guide.md) for a step-by-step guide.

## Running the tests

```bash
python3 -m unittest discover -s tests -v
```

The same command runs in the [Tests workflow](.github/workflows/tests.yml) on GitHub Actions.

## Project structure

```
student-task-manager/
├── main.py                 # console menu
├── task_manager.py         # Task and TaskManager logic
├── tests/                  # unittest test suite
├── docs/user-guide.md      # user guide
├── lab-evidence/           # screenshots and command output for the lab
├── LAB-REPORT.md           # assignment report
└── .github/workflows/      # GitHub Actions workflow
```

## Roadmap

- Due dates for tasks
- Sorting tasks by status

## License

MIT, see [LICENSE](LICENSE).
