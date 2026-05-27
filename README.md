# Task Tracker CLI

A simple Command Line Interface (CLI) task tracker built with Python.

This project allows users to manage tasks directly from the terminal without using a graphical interface.

---

# Features

- Add new tasks
- Update existing tasks
- Delete tasks
- Mark tasks as:
  - todo
  - in-progress
  - done
- List all tasks
- Filter tasks by status
- Store data in a JSON file
- Automatic JSON file creation
- Edge case handling

---

# Technologies Used

- Python
- JSON
- File Handling
- Command Line Arguments (sys.argv)

---

# Project Structure

task-tracker/
│
├── main.py
└── tasks.json
---

# How To Run

Open terminal inside the project folder.

## Add Task

python main.py add "Study Python"
---

## List Tasks

python main.py list
---

## List Done Tasks

python main.py list done
---

## Update Task

python main.py update 1 "Study Machine Learning"
---

## Delete Task

python main.py delete 1
---

## Mark Task As Done

python main.py mark-done 1
---

## Mark Task As In Progress

python main.py mark-in-progress 1
---

# Example JSON Data

[
    {
        "id": 1,
        "description": "Study Python",
        "status": "done",
        "createdAt": "2026-05-27 10:00:00",
        "updatedAt": "2026-05-27 11:00:00"
    }
]
---

# Concepts Practiced

This project helped practice:

- Python functions
- Lists and dictionaries
- List comprehensions
- JSON handling
- File handling
- Error handling
- CRUD operations
- CLI application development

---

# Future Improvements

Possible future upgrades:

- Colorful terminal output
- Due dates
- Task priorities
- Search functionality
- SQLite database support
- Interactive menu system

---

# Author

Sepehr Abrishamchi