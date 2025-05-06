from src.app import app
from fastapi.testclient import TestClient

def test_hello_world():
    client = TestClient(app)
    response = client.get("/hello-world")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, World!"}
