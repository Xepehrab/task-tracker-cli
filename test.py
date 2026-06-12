from unittest.mock import patch
from main import (
    load_tasks,
    add_task,
    update_task,
    delete_task,
    change_status,
    list_tasks,
)


def test_load_tasks_file_not_exists():
    with patch("os.path.exists", return_value=False):
        assert load_tasks() == []


def test_add_task():
    with patch("main.load_tasks", return_value=[]), \
         patch("main.save_tasks") as mock_save:

        add_task("Learn Python")

        saved_tasks = mock_save.call_args[0][0]

        assert len(saved_tasks) == 1
        assert saved_tasks[0]["id"] == 1
        assert saved_tasks[0]["description"] == "Learn Python"
        assert saved_tasks[0]["status"] == "todo"


def test_update_task():
    tasks = [
        {
            "id": 1,
            "description": "Old task",
            "status": "todo",
            "createdAt": "time",
            "updatedAt": "time",
        }
    ]

    with patch("main.load_tasks", return_value=tasks), \
         patch("main.save_tasks") as mock_save:

        update_task(1, "New task")

        saved_tasks = mock_save.call_args[0][0]

        assert saved_tasks[0]["description"] == "New task"


def test_delete_task():
    tasks = [
        {
            "id": 1,
            "description": "Task",
            "status": "todo",
            "createdAt": "time",
            "updatedAt": "time",
        }
    ]

    with patch("main.load_tasks", return_value=tasks), \
         patch("main.save_tasks") as mock_save:

        delete_task(1)

        saved_tasks = mock_save.call_args[0][0]

        assert saved_tasks == []


def test_change_status():
    tasks = [
        {
            "id": 1,
            "description": "Task",
            "status": "todo",
            "createdAt": "time",
            "updatedAt": "time",
        }
    ]

    with patch("main.load_tasks", return_value=tasks), \
         patch("main.save_tasks") as mock_save:

        change_status(1, "done")

        saved_tasks = mock_save.call_args[0][0]

        assert saved_tasks[0]["status"] == "done"


def test_list_tasks(capsys):
    tasks = [
        {
            "id": 1,
            "description": "Learn pytest",
            "status": "todo",
            "createdAt": "time",
            "updatedAt": "time",
        }
    ]

    with patch("main.load_tasks", return_value=tasks):
        list_tasks()

    captured = capsys.readouterr()

    assert "Learn pytest" in captured.out


def test_update_task_not_found(capsys):
    with patch("main.load_tasks", return_value=[]):
        update_task(99, "New text")

    captured = capsys.readouterr()

    assert "not found" in captured.out


def test_delete_task_not_found(capsys):
    with patch("main.load_tasks", return_value=[]):
        delete_task(99)

    captured = capsys.readouterr()

    assert "Can't find task" in captured.out


def test_change_status_not_found(capsys):
    with patch("main.load_tasks", return_value=[]):
        change_status(99, "done")

    captured = capsys.readouterr()

    assert "Can't find task" in captured.out


def test_list_tasks_empty(capsys):
    with patch("main.load_tasks", return_value=[]):
        list_tasks()

    captured = capsys.readouterr()

    assert "No tasks found" in captured.out