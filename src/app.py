from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np
import logging
from .config import MODEL_PATH, ENCODER_PATH, LOG_LEVEL

# Configure logging
logging.basicConfig(level=LOG_LEVEL)
logger = logging.getLogger(__name__)

# Load saved model + encoder
try:
    model = joblib.load(MODEL_PATH)
    label_encoder = joblib.load(ENCODER_PATH)
    logger.info("Models loaded successfully")
except FileNotFoundError as e:
    logger.error(f"Failed to load models: {e}")
    raise

app = FastAPI(title="Iris Classifier API", version="1.0.0")

class IrisFeatures(BaseModel):
    SepalLengthCm: float
    SepalWidthCm: float
    PetalLengthCm: float
    PetalWidthCm: float

@app.get("/")
def root():
    return {"message": "Iris classifier is running"}

@app.post("/predict")
def predict(features: IrisFeatures):
    X = np.array([[
        features.SepalLengthCm,
        features.SepalWidthCm,
        features.PetalLengthCm,
        features.PetalWidthCm
    ]])

    pred_encoded = model.predict(X)[0]
    pred_label = label_encoder.inverse_transform([pred_encoded])[0]

    return {"prediction": pred_label}

