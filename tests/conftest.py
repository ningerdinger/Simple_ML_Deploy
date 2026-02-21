"""Test configuration."""
import pytest
import os
import sys

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

@pytest.fixture
def client():
    """Create a test client."""
    from fastapi.testclient import TestClient
    from src.app import app
    return TestClient(app)
