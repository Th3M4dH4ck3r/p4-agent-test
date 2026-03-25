import pytest
from app import app, users

@pytest.fixture(autouse=True)
def clear_users():
    users.clear()
    yield
    users.clear()

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

def test_get_user(client):
    r = client.post("/users", json={"name": "Alice", "email": "alice@example.com"})
    uid = r.json["id"]
    r = client.get(f"/users/{uid}")
    assert r.status_code == 200
    assert r.json["name"] == "Alice"
    assert r.json["email"] == "alice@example.com"

def test_get_user_not_found(client):
    r = client.get("/users/999")
    assert r.status_code == 404

def test_update_user(client):
    r = client.post("/users", json={"name": "Bob", "email": "bob@example.com"})
    uid = r.json["id"]
    r = client.put(f"/users/{uid}", json={"name": "Robert", "email": "robert@example.com"})
    assert r.status_code == 200
    assert r.json["name"] == "Robert"
    assert r.json["email"] == "robert@example.com"

def test_update_user_partial(client):
    r = client.post("/users", json={"name": "Carol", "email": "carol@example.com"})
    uid = r.json["id"]
    r = client.put(f"/users/{uid}", json={"name": "Caroline"})
    assert r.status_code == 200
    assert r.json["name"] == "Caroline"
    assert r.json["email"] == "carol@example.com"

def test_update_user_not_found(client):
    r = client.put("/users/999", json={"name": "Ghost"})
    assert r.status_code == 404
