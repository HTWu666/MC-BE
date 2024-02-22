import pytest
from app import app
from models.tasks import Task


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client
        Task.tasks_list.clear()


def test_delete_task_success(client):
    """Test successfully deleting a task"""
    Task.tasks_list.append({"id": 1, "name": "Task to be deleted", "status": True})
    response = client.delete("/api/v1/task/1")
    assert response.status_code == 200
    assert "Task #1 has been deleted" in response.get_json()["message"]
    assert len(Task.tasks_list) == 0


def test_delete_task_not_exist(client):
    """Test deleting a non-existent task"""
    task_id = 999
    response = client.delete(f"/api/v1/task/{task_id}")
    assert response.status_code == 400
    assert f"Task with ID {task_id} does not exist." in response.get_json()["errors"]


@pytest.mark.parametrize("task_id", ["a", "-1", "1.5"])
def test_delete_task_invalid_id(client, task_id):
    """Test deleting a task with invalid ID types such as string, negative number, or float."""
    response = client.delete(f"/api/v1/task/{task_id}")
    assert (
        response.status_code == 404
    ), f"Response status code was not 404 for task_id={task_id}"
