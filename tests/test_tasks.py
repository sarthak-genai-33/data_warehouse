from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_get_tasks():
    response = client.get("/tasks")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_cancel_tasks():
    response = client.post("/tasks/cancel", json={"task_id": "123"})
    assert response.status_code == 200
    assert response.json() == {"message": "Task 123 cancelled"}
