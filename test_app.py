import pytest
from app import app, users

@pytest.fixture
def client():
    app.config["TESTING"] = True
    users.clear()
    with app.test_client() as c:
        yield c

def test_create_task(client):
    r = client.post("/tasks", json={"title": "Buy milk"})
    assert r.status_code == 201
    assert r.json["title"] == "Buy milk"

def test_list_tasks(client):
    r = client.get("/tasks")
    assert r.status_code == 200

def test_get_user_profile(client):
    r = client.post("/users", json={"name": "Alice", "email": "alice@example.com"})
    uid = r.json["id"]
    r = client.get(f"/users/{uid}")
    assert r.status_code == 200
    assert r.json["name"] == "Alice"
    assert r.json["email"] == "alice@example.com"

def test_get_user_profile_not_found(client):
    r = client.get("/users/999")
    assert r.status_code == 404

def test_update_user_profile(client):
    r = client.post("/users", json={"name": "Bob", "email": "bob@example.com"})
    uid = r.json["id"]
    r = client.put(f"/users/{uid}", json={"name": "Bobby", "email": "bobby@example.com"})
    assert r.status_code == 200
    assert r.json["name"] == "Bobby"
    assert r.json["email"] == "bobby@example.com"

def test_update_user_profile_not_found(client):
    r = client.put("/users/999", json={"name": "Ghost"})
    assert r.status_code == 404
