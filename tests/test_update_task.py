from unittest.mock import patch
import pytest
from app import app
from models.tasks import Task

API_VERSION = "/api/v1"


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client
        Task.tasks_dict.clear()


def test_update_task_success(client):
    """Test successfully updating a task"""
    Task.tasks_dict[1] = {"name": "Original Task", "status": True}
    response = client.put(
        f"{API_VERSION}/task/1", json={"id": 1, "name": "Updated Task", "status": False}
    )
    assert response.status_code == 200
    assert Task.tasks_dict[1]["name"] == "Updated Task"


def test_update_task_id_mismatch(client):
    """Test when id in query string is different from id in request body"""
    Task.tasks_dict[1] = {"name": "Original Task", "status": True}
    response = client.put(
        f"{API_VERSION}/task/2", json={"id": 1, "name": "Updated Task", "status": False}
    )
    assert response.status_code == 400
    assert (
        "ID in URL does not match ID in request body." in response.get_json()["errors"]
    )


def test_update_task_not_exist(client):
    """Test updating a non-existent task"""
    task_id = 1
    response = client.put(
        f"{API_VERSION}/task/1",
        json={"id": task_id, "name": "Nonexistent Task", "status": False},
    )
    assert response.status_code == 400
    assert f"Task with ID {task_id} does not exist" in response.get_json()["errors"]


@pytest.mark.parametrize(
    "data, expected_status",
    [
        ({"id": 1, "name": "", "status": True}, 400),  # test the name is null
        (
            {"id": -1, "name": "Test Task", "status": True},
            404,
        ),  # test id is a negative number
        (
            {"id": 1.1, "name": "Test Task", "status": True},
            404,
        ),  # test id is a floating point number
        (
            {"id": 1, "name": "Test Task", "status": 2},
            400,
        ),  # test status is not boolean
        (
            {"id": 1, "name": "a" * 51, "status": True},
            400,
        ),  # test the length of name exceed 50 character
    ],
)
def test_update_task_validation_errors(client, data, expected_status):
    """Test boundary conditions for all fields"""
    if data["id"] > 0:
        Task.tasks_dict.clear()
        Task.tasks_dict[1] = {"name": "Original Task", "status": True}

    response = client.put(f"{API_VERSION}/task/{data['id']}", json=data)
    assert (
        response.status_code == expected_status
    ), f"Expected status code {expected_status} but got {response.status_code}"


def test_update_task_unexpected_error(client):
    """Test updating a task encountering unexpected error"""
    Task.tasks_dict[1] = {"name": "Original Task", "status": True}

    with patch("models.tasks.Task.update") as mock_update:
        mock_update.side_effect = Exception("Unexpected error")
        response = client.put(
            f"{API_VERSION}/task/1",
            json={"id": 1, "name": "Updated Task", "status": True},
        )

        assert (
            response.status_code == 500
        ), "Expected a 500 status code for an internal server error"

        data = response.get_json()
        assert "errors" in data, "Expected the response to contain an 'errors' key"
