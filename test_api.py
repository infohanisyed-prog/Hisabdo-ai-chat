from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"

def test_chat_and_history():
    response = client.post("/chat", json={"conversation_id": "test-1", "message": "How do I add an expense?"})
    assert response.status_code == 200
    data = response.json()
    assert data["response"]
    assert "expense-001" in data["sources"]

    history = client.get("/conversations/test-1/messages")
    assert history.status_code == 200
    assert len(history.json()["messages"]) == 2
