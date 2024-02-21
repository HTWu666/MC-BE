import pytest
from app import app
from blueprints.tasks import tasks_list


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_get_tasks(client):
    """Test successfully getting the task list"""
    tasks_list.append({"id": 1, "name": "Test Task", "status": 0})

    response = client.get("/api/v1/tasks")

    assert response.status_code == 200

    json_data = response.get_json()
    assert "result" in json_data
    assert len(json_data["result"]) == len(tasks_list)
    assert json_data["result"][0]["name"] == "Test Task"
