import sys
from pathlib import Path

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