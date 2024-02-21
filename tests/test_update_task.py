import pytest
from app import app
from blueprints.tasks import tasks_list


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client
        tasks_list.clear()


def test_update_task_success(client):
    """Test successfully updating a task"""
    tasks_list.append({"id": 1, "name": "Original Task", "status": True})
    response = client.put(
        "/api/v1/task/1", json={"id": 1, "name": "Updated Task", "status": False}
    )
    assert response.status_code == 200
    assert tasks_list[0]["name"] == "Updated Task"


def test_update_task_id_mismatch(client):
    """Test when id in query string is different from id in request body"""
    tasks_list.append({"id": 1, "name": "Test Task", "status": True})
    response = client.put(
        "/api/v1/task/2", json={"id": 1, "name": "Updated Task", "status": False}
    )
    assert response.status_code == 400
    assert (
        "ID in URL does not match ID in request body." in response.get_json()["errors"]
    )


def test_update_task_not_exist(client):
    """Test updating a non-existent task"""
    response = client.put(
        "/api/v1/task/1", json={"id": 1, "name": "Nonexistent Task", "status": False}
    )
    assert response.status_code == 400
    assert "The updated task doesn't exist." in response.get_json()["errors"]


@pytest.mark.parametrize(
    "data, expected_status",
    [
        ({"id": 1, "name": "", "status": True}, 400),  # test the name is null
        ({"id": -1, "name": "Test Task", "status": True}, 404),  # test id is negative
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
        tasks_list.clear()
        tasks_list.append({"id": 1, "name": "Original Task", "status": True})

    response = client.put(f"/api/v1/task/{data['id']}", json=data)
    assert (
        response.status_code == expected_status
    ), f"Expected status code {expected_status} but got {response.status_code}"
