import sys
from pathlib import Path
from unittest.mock import MagicMock, Mock

sys.path.insert(0, str(Path(__file__).parent.parent))

from app.services.ml_service import MLService


def test_predict_with_loaded_models():
    service = MLService.__new__(MLService)

    service.model_category = MagicMock()
    service.model_priority = MagicMock()

    service.model_category.__bool__ = lambda self: True
    service.model_priority.__bool__ = lambda self: True

    service.model_category.predict.return_value = ["technical"]
    service.model_priority.predict.return_value = ["high"]

    mock_cat_proba = MagicMock()
    mock_cat_proba.max.return_value = 0.9
    service.model_category.predict_proba.return_value = mock_cat_proba

    mock_prio_proba = MagicMock()
    mock_prio_proba.max.return_value = 0.8
    service.model_priority.predict_proba.return_value = mock_prio_proba

    result = service.predict("My app keeps crashing")

    assert result["category"] == "technical"
    assert result["priority"] == "high"
    assert result["confidence"] == 0.85


def test_predict_billing_category():
    service = MLService.__new__(MLService)

    service.model_category = MagicMock()
    service.model_priority = MagicMock()

    service.model_category.__bool__ = lambda self: True
    service.model_priority.__bool__ = lambda self: True

    service.model_category.predict.return_value = ["billing"]
    service.model_priority.predict.return_value = ["medium"]

    mock_cat_proba = MagicMock()
    mock_cat_proba.max.return_value = 0.95
    service.model_category.predict_proba.return_value = mock_cat_proba

    mock_prio_proba = MagicMock()
    mock_prio_proba.max.return_value = 0.85
    service.model_priority.predict_proba.return_value = mock_prio_proba

    result = service.predict("I was charged twice")

    assert result["category"] == "billing"
    assert result["priority"] == "medium"
    assert result["confidence"] == 0.9


def test_predict_without_models():
    service = MLService.__new__(MLService)
    service.model_category = None
    service.model_priority = None

    result = service.predict("Some text")

    assert result["category"] == "other"
    assert result["priority"] == "medium"
    assert result["confidence"] == 0.0


def test_predict_handles_exception():
    service = MLService.__new__(MLService)

    service.model_category = MagicMock()
    service.model_priority = MagicMock()

    service.model_category.__bool__ = lambda self: True
    service.model_priority.__bool__ = lambda self: True

    service.model_category.predict.side_effect = Exception("Model error!")

    result = service.predict("Test text")

    assert result["category"] == "other"
    assert result["priority"] == "medium"
    assert result["confidence"] == 0.0
