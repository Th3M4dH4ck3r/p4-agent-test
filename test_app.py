import pytest
from app import app

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as c:
        yield c

def test_create_task(client):
    r = client.post("/tasks", json={"title": "Buy milk"})
    assert r.status_code == 201
    assert r.json["title"] == "Buy milk"

def test_list_tasks(client):
    r = client.get("/tasks")
    assert r.status_code == 200
