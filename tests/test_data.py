from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_get_data():
    response = client.get("/data")
    assert response.status_code == 200
    assert "customers" in response.json()
    assert "campaigns" in response.json()
