import copy
import pytest
from fastapi.testclient import TestClient

from src.app import app, activities

# Save a deep copy of initial activities state
_INITIAL_ACTIVITIES = copy.deepcopy(activities)


@pytest.fixture(autouse=True)
def reset_activities():
    """Reset the in-memory activities dictionary before each test."""
    activities.clear()
    activities.update(copy.deepcopy(_INITIAL_ACTIVITIES))


@pytest.fixture
def client():
    """Fixture to provide a TestClient for FastAPI app."""
    return TestClient(app)
