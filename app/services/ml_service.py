import joblib
from pathlib import Path


class MLService:
    def __init__(self):
        current_file_path = Path(__file__).resolve()
        project_root = current_file_path.parent.parent.parent
        self.model_dir = project_root / "models"

        self.model_category = None
        self.model_priority = None

        self.load_models()

    def load_models(self):
        cat_path = self.model_dir / "model_category.joblib"
        prio_path = self.model_dir / "model_priority.joblib"

        if cat_path.exists() and prio_path.exists():
            try:
                self.model_category = joblib.load(cat_path)
                self.model_priority = joblib.load(prio_path)
                return True
            except Exception:
                return False
        return False

    def predict(self, text: str):
        if not self.model_category or not self.model_priority:
            return {"category": "other", "priority": "medium", "confidence": 0.0}

        try:
            category = self.model_category.predict([text])[0]
            priority = self.model_priority.predict([text])[0]

            cat_prob = self.model_category.predict_proba([text]).max()
            prio_prob = self.model_priority.predict_proba([text]).max()

            avg_confidence = (cat_prob + prio_prob) / 2

            return {
                "category": category,
                "priority": priority,
                "confidence": round(float(avg_confidence), 2),
            }
        except Exception:
            return {"category": "other", "priority": "medium", "confidence": 0.0}


ml_service = MLService()
