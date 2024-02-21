import pytest
from app import app
from blueprints.tasks import tasks_list


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client
        tasks_list.clear()


def test_delete_task_success(client):
    """Test successfully deleting a task"""
    tasks_list.append({"id": 1, "name": "Task to be deleted", "status": True})
    response = client.delete("/api/v1/task/1")
    assert response.status_code == 200
    assert "Task #1 has been deleted" in response.get_json()["message"]
    assert len(tasks_list) == 0


def test_delete_task_not_exist(client):
    """Test deleting a non-existent task"""
    response = client.delete("/api/v1/task/999")
    assert response.status_code == 400
    assert "The deleted task doesn't exist." in response.get_json()["errors"]
