"""Command-line task manager that stores tasks in a local JSON file."""

import sys
import json
import os
from datetime import datetime

FILE_NAME = "task.json"


def load_tasks():
    """Load all tasks from the JSON file.

    Returns:
        list[dict]: Task records, or an empty list if the file is missing or invalid.
    """
    if not os.path.exists(FILE_NAME):
        return []
    try:
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            return json.load(file)
    except json.JSONDecodeError:
        return []


def save_tasks(tasks):
    """Write the full task list to the JSON file.

    Args:
        tasks (list[dict]): Tasks to persist.
    """
    with open(FILE_NAME, "w", encoding="utf-8") as file:
        json.dump(tasks, file, indent=4)


def add_task(description):
    """Add a new task with status ``todo``.

    Args:
        description (str): Text describing the task.
    """
    tasks = load_tasks()

    task_id = max(task["id"] for task in tasks) + 1 if tasks else 1
    current_time = datetime.now().isoformat()

    task_dict = {
        "id": task_id,
        "description": description,
        "status": "todo",
        "createdAt": current_time,
        "updatedAt": current_time,
    }
    tasks.append(task_dict)
    save_tasks(tasks)
    print(f"Task {description} added successfully (ID: {task_id})")


def update_task(task_id, new_description):
    """Update a task's description.

    Args:
        task_id (int): ID of the task to update.
        new_description (str): New description text.
    """
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["description"] = new_description
            task["updatedAt"] = datetime.now().isoformat()
            save_tasks(tasks)
            print(f"Task {task_id} updated successfully")
            return
    print(f"Task with ID {task_id} not found")


def delete_task(task_id):
    """Remove a task by ID.

    Args:
        task_id (int): ID of the task to delete.
    """
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            save_tasks(tasks)
            print(f"Task {task_id} removed successfully")
            return
    print(f"Can't find task {task_id}")


def change_status(task_id, new_status):
    """Change a task's status.

    Args:
        task_id (int): ID of the task to update.
        new_status (str): New status value (e.g. ``todo``, ``in-progress``, ``done``).
    """
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["status"] = new_status
            task["updatedAt"] = datetime.now().isoformat()
            save_tasks(tasks)
            print(f"Task {task_id} status updated successfully")
            return
    print(f"Can't find task {task_id}")


def list_tasks(status_filter=None):
    """Print tasks, optionally filtered by status.

    Args:
        status_filter (str | None): If set, only tasks with this status are shown.
    """
    tasks = load_tasks()
    if not tasks:
        print("No tasks found. Add one and try again.")
        return

    found = False
    for task in tasks:
        if status_filter is None or task["status"] == status_filter:
            print(
                f"ID: {task['id']} | "
                f"Status: [{task['status']}] | "
                f"{task['description']}"
            )
            found = True

    if status_filter and not found:
        print(f"No task with status {status_filter} found")

    print("-------------------\n")


def main():
    """Parse CLI arguments and dispatch to the appropriate command handler."""
    if len(sys.argv) < 2:
        print("Usage: python task_cli.py <command> [arguments]")
        return

    command = sys.argv[1]

    if command == "add":
        if len(sys.argv) < 3:
            print("Error: please provide a task description")
        else:
            add_task(sys.argv[2])

    elif command == "update":
        if len(sys.argv) < 4:
            print("Error: please enter task id and description")
        else:
            update_task(int(sys.argv[2]), sys.argv[3])

    elif command == "delete":
        if len(sys.argv) < 3:
            print("Error: please provide a task ID")
        else:
            delete_task(int(sys.argv[2]))

    elif command == "in-progress":
        if len(sys.argv) < 3:
            print("Error: please provide a task ID")
        else:
            change_status(int(sys.argv[2]), "in-progress")

    elif command == "done":
        if len(sys.argv) < 3:
            print("Error: please provide a task ID")
        else:
            change_status(int(sys.argv[2]), "done")

    elif command == "list":
        if len(sys.argv) == 3:
            list_tasks(sys.argv[2])
        else:
            list_tasks()

    else:
        print(f"Unknown command: {command}")


if __name__ == "__main__":
    main()
