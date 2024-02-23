import pytest
from app import app


@pytest.fixture
def client():
    with app.test_client() as client:
        yield client


def test_404_page_not_found(client):
    """Testing access to a non-existent route"""
    response = client.get("/api/nonexistent")
    assert response.status_code == 404


def test_global_exception_handler(client):
    """Test global exception handler"""
    response = client.get("/test/error")
    assert response.status_code == 500
