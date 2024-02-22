from unittest.mock import patch
import pytest
from app import app
from models.tasks import Task


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_get_tasks(client):
    """Test successfully getting the task list"""
    Task.tasks_dict[1] = {"name": "Test Task", "status": False}

    response = client.get("/tasks")

    assert response.status_code == 200

    json_data = response.get_json()
    assert "result" in json_data
    assert len(json_data["result"]) == len(Task.tasks_dict)
    assert json_data["result"][0]["name"] == "Test Task"


def test_get_tasks_unexpected_error(client):
    """Test fetching task list encountering unexpected error"""
    with patch("models.tasks.Task.get_all") as mock_get_all:
        mock_get_all.side_effect = Exception("Unexpected error")
        response = client.get("/tasks")

        assert (
            response.status_code == 500
        ), "Expected a 500 status code for an internal server error"

        json_data = response.get_json()
        assert "errors" in json_data, "Expected the response to contain an 'errors' key"
