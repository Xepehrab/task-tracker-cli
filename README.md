# Task Tracker CLI
A simple command-line application built with Python for managing daily tasks directly from the terminal.
Tasks are stored locally in a JSON file and support basic operations such as adding, updating, deleting, and tracking task status.
## Features
- Add new tasks
- Update existing tasks
- Delete tasks
- Mark tasks as `todo`, `in-progress`, or `done`
- List all tasks
- Filter tasks by status
- Automatic JSON file creation on first run
- Persistent task storage using JSON
## Project Structure
```
task-tracker/
│
├── main.py
├── tasks.json
├── README.md
└── .gitignore
```
## Requirements
- Python 3.x
- No external libraries required
## Installation
```bash
git clone https://github.com/Xepehrab/task-tracker-cli
cd task-tracker-cli
```
## Usage
```bash
# Add a task
python main.py add "Study Python"
# List all tasks
python main.py list
# List tasks by status (todo | in-progress | done)
python main.py list done
# Update a task
python main.py update 1 "Study Machine Learning"
# Delete a task
python main.py delete 1
# Mark task as done
python main.py mark-done 1
# Mark task as in progress
python main.py mark-in-progress 1
```
## Task Statuses
| Status        | Description                   |
|---------------|-------------------------------|
| `todo`        | Task has not been started     |
| `in-progress` | Task is currently in progress |
| `done`        | Task is completed             |

## Example Data
```json
[
    {
        "id": 1,
        "description": "Study Python",
        "status": "done",
        "createdAt": "2026-05-27 10:00:00",
        "updatedAt": "2026-05-27 11:00:00"
    }
]
```