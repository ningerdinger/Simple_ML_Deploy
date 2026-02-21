"""Configuration module for the Iris Classifier API."""
import os
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, "data")
MODEL_PATH = os.path.join(BASE_DIR, "iris_model.joblib")
ENCODER_PATH = os.path.join(BASE_DIR, "label_encoder.joblib")

API_HOST = os.getenv("API_HOST", "0.0.0.0")
API_PORT = int(os.getenv("API_PORT", "8000"))
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
