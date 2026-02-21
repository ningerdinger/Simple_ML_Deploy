# Iris Classifier API

A FastAPI-based REST API for classifying Iris flowers using machine learning models trained on the classic Iris dataset.

## Project Overview

This project implements a machine learning pipeline that:
- Trains classification models (Decision Tree and Random Forest) on the Iris dataset
- Exposes predictions via a REST API
- Provides interactive API documentation

## Project Structure

```
├── iris.csv              # Iris dataset
├── train_model.py        # Model training script
├── app.py                # FastAPI application
├── requirements.txt      # Python dependencies
├── Dockerfile            # Docker configuration
└── iris_model.joblib     # Trained model (generated)
└── label_encoder.joblib  # Label encoder (generated)
```

## Requirements

- Python 3.13+
- pandas
- numpy
- scikit-learn
- fastapi
- uvicorn
- joblib

## Installation

1. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Training the Model

Run the training script to train and save the classification models:
```bash
python train_model.py
```

This will:
- Load the Iris dataset from `iris.csv`
- Train Decision Tree and Random Forest classifiers
- Save the trained model and label encoder as joblib files

### Running the API

Start the FastAPI server:
```bash
python -m uvicorn app:app --reload
```

The server will start on `http://127.0.0.1:8000`

### API Endpoints

#### GET /
Returns a simple status message:
```json
{"message": "Iris classifier is running"}
```

#### POST /predict
Predicts the Iris species based on flower measurements.

**Request Body:**
```json
{
  "SepalLengthCm": 5.1,
  "SepalWidthCm": 3.5,
  "PetalLengthCm": 1.4,
  "PetalWidthCm": 0.2
}
```

**Response:**
```json
{"prediction": "Iris-setosa"}
```

## API Documentation

Once the server is running, access the interactive API documentation:
- **Swagger UI**: http://127.0.0.1:8000/docs
- **ReDoc**: http://127.0.0.1:8000/redoc

## Docker

Build and run with Docker:
```bash
docker build -t iris-classifier .
docker run -p 8000:8000 iris-classifier
```

### Complete Docker Workflow

Follow these steps to build and test the containerized application:

**Step 1: Build the Docker Image**
```bash
docker build -t iris-classifier .
```

This command reads the Dockerfile and creates an image named `iris-classifier` with all dependencies installed.

**Step 2: Run the Container**
```bash
docker run -p 8000:8000 iris-classifier
```

This starts the container and maps port 8000 from the container to your localhost, making the API accessible at `http://localhost:8000`.

**Step 3: Verify the Server is Running**

Open your browser and navigate to:
- http://localhost:8000/docs - Interactive Swagger UI
- http://localhost:8000/ - Root endpoint test

**Step 4: Make a Prediction**

Using PowerShell:
```powershell
$body = "{`"SepalLengthCm`": 5.1, `"SepalWidthCm`": 3.5, `"PetalLengthCm`": 1.4, `"PetalWidthCm`": 0.2}"; Invoke-WebRequest -Uri "http://localhost:8000/predict" -Method POST -Headers @{"Content-Type"="application/json"} -Body $body -UseBasicParsing | Select-Object -ExpandProperty Content
```

Expected output:
```json
{"prediction":"Iris-setosa"}
```

### Making Predictions with Docker

Once the container is running, you can make predictions using:

**Using curl:**
```bash
curl -X POST "http://localhost:8000/predict" \
  -H "Content-Type: application/json" \
  -d '{
    "SepalLengthCm": 5.1,
    "SepalWidthCm": 3.5,
    "PetalLengthCm": 1.4,
    "PetalWidthCm": 0.2
  }'
```

**Using Python requests:**
```python
import requests

url = "http://localhost:8000/predict"
data = {
    "SepalLengthCm": 5.1,
    "SepalWidthCm": 3.5,
    "PetalLengthCm": 1.4,
    "PetalWidthCm": 0.2
}
response = requests.post(url, json=data)
print(response.json())
```

**Using the interactive UI:**
Open your browser and go to `http://localhost:8000/docs` to access the Swagger UI where you can make requests directly.

## Notes

- Measurements should be in centimeters
- The model expects 4 features: Sepal Length, Sepal Width, Petal Length, Petal Width
- Possible predictions: Iris-setosa, Iris-versicolor, Iris-virginica 