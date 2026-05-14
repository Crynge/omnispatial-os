from fastapi.testclient import TestClient

from services.omnispatial_api.app.main import app


client = TestClient(app)


def test_health() -> None:
    response = client.get("/health")
    assert response.status_code == 200


def test_agents() -> None:
    response = client.get("/api/agents")
    assert response.status_code == 200
    assert response.json()["items"]

