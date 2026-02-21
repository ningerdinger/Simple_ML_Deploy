from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

# Load saved model + encoder
model = joblib.load("iris_model.joblib")
label_encoder = joblib.load("label_encoder.joblib")

app = FastAPI(title="Iris Classifier API")

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
