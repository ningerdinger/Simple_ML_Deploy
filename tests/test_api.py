"""Tests for the Iris Classifier API."""

def test_root(client):
    """Test root endpoint."""
    response = client.get("/")
    assert response.status_code == 200
    assert "message" in response.json()

def test_predict(client):
    """Test predict endpoint."""
    payload = {
        "SepalLengthCm": 5.1,
        "SepalWidthCm": 3.5,
        "PetalLengthCm": 1.4,
        "PetalWidthCm": 0.2
    }
    response = client.post("/predict", json=payload)
    assert response.status_code == 200
    assert "prediction" in response.json()
    prediction = response.json()["prediction"]
    assert prediction in ["Iris-setosa", "Iris-versicolor", "Iris-virginica"]

def test_predict_invalid(client):
    """Test predict with invalid input."""
    payload = {"SepalLengthCm": "invalid"}
    response = client.post("/predict", json=payload)
    assert response.status_code == 422  # Validation error
