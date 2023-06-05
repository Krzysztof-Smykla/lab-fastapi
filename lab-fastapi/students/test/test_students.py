from fastapi.testclient import TestClient
import pytest

from main import app

client = TestClient(app)


def test_get_students():
    response = client.get("/students")
    assert response.status_code == 200
    assert response.json() == []

@pytest.fixture(autouse=True)
def delete_all_students():
    for student in client.get("/students").json():
        client.delete(f"/students/{student['id']}")
