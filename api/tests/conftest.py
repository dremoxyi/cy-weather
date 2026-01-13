import sys
from pathlib import Path

import pytest
from fastapi.testclient import TestClient

# Add parent directory to path so we can import main
sys.path.insert(0, str(Path(__file__).parent.parent))

from main import app

@pytest.fixture
def client():
    return TestClient(app)
