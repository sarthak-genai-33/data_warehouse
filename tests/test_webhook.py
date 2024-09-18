from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_receive_webhook():
    response = client.post("/webhook", json={"customer": {"name": "John Doe", "email": "john@example.com"}})
    assert response.status_code == 200
    assert response.json() == {"message": "Data received successfully"}
