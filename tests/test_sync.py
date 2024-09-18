from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_trigger_sync():
    response = client.get("/sync/crm")
    assert response.status_code == 200
    assert response.json() == {"message": "Sync triggered for crm"}
