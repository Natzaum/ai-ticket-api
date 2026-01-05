import sys
from pathlib import Path
from unittest.mock import patch

project_root = Path(__file__).parent.parent
app_path = project_root / "app"

sys.path.insert(0, str(project_root))
sys.path.insert(0, str(app_path))

from app.main import app
from fastapi.testclient import TestClient

client = TestClient(app)


def test_root_endpoint():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {"API": "Alive"}


@patch("app.main.ml_service.predict")
def test_classify_ticket_happy_path(mock_predict):
    mock_predict.return_value = {
        "category": "technical",
        "priority": "high",
        "confidence": 0.85,
    }

    ticket_data = {"description": "My application keeps crashing when I try to log in"}
    response = client.post("/tickets/classify", json=ticket_data)

    assert response.status_code == 200
    data = response.json()
    assert data["category"] == "technical"
    assert data["priority"] == "high"
    assert data["confidence"] == 0.85


@patch("app.main.ml_service.predict")
def test_classify_billing_ticket(mock_predict):
    mock_predict.return_value = {
        "category": "billing",
        "priority": "medium",
        "confidence": 0.92,
    }

    ticket_data = {"description": "I was charged twice for my subscription this month"}
    response = client.post("/tickets/classify", json=ticket_data)

    assert response.status_code == 200
    data = response.json()
    assert data["category"] == "billing"
    assert data["priority"] == "medium"


def test_classify_description_too_short():
    ticket_data = {"description": "Too short"}
    response = client.post("/tickets/classify", json=ticket_data)

    assert response.status_code == 422


def test_classify_description_too_long():
    ticket_data = {"description": "x" * 1501}
    response = client.post("/tickets/classify", json=ticket_data)

    assert response.status_code == 422


def test_classify_missing_description():
    ticket_data = {}
    response = client.post("/tickets/classify", json=ticket_data)

    assert response.status_code == 422


@patch("app.main.ml_service.predict")
def test_classify_minimum_valid_length(mock_predict):
    mock_predict.return_value = {
        "category": "other",
        "priority": "low",
        "confidence": 0.65,
    }

    ticket_data = {"description": "1234567890"}
    response = client.post("/tickets/classify", json=ticket_data)

    assert response.status_code == 200


@patch("app.main.ml_service.predict")
def test_classify_maximum_valid_length(mock_predict):
    mock_predict.return_value = {
        "category": "feature request",
        "priority": "low",
        "confidence": 0.78,
    }

    ticket_data = {"description": "x" * 1500}
    response = client.post("/tickets/classify", json=ticket_data)

    assert response.status_code == 200
