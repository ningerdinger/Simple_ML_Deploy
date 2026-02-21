import pandas as pd
import joblib
import logging
import os
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from .config import DATA_DIR, MODEL_PATH, ENCODER_PATH

# Configure logging
logging.basicConfig(level="INFO")
logger = logging.getLogger(__name__)

def train():
    """Train and save the iris classification model."""
    logger.info("Starting model training...")
    
    # Load dataset from data/
    iris_path = os.path.join(DATA_DIR, "iris.csv")
    if not os.path.exists(iris_path):
        raise FileNotFoundError(f"Data file not found: {iris_path}")
    
    df = pd.read_csv(iris_path)
    df = df.drop(columns=["Id"])
    logger.info(f"Loaded dataset with {len(df)} samples")

    # Split features/labels
    X = df.drop("Species", axis=1)
    y = df["Species"]

    # Encode labels
    le = LabelEncoder()
    y_encoded = le.fit_transform(y)
    logger.info(f"Classes: {le.classes_}")

    # Train/test split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y_encoded, test_size=0.2, random_state=42
    )
    logger.info(f"Training set: {len(X_train)}, Test set: {len(X_test)}")

    # Train model
    logger.info("Training Random Forest model...")
    model = RandomForestClassifier(n_estimators=200, random_state=42)
    model.fit(X_train, y_train)
    
    # Evaluate
    train_score = model.score(X_train, y_train)
    test_score = model.score(X_test, y_test)
    logger.info(f"Train accuracy: {train_score:.4f}, Test accuracy: {test_score:.4f}")

    # Save artifacts
    joblib.dump(model, MODEL_PATH)
    joblib.dump(le, ENCODER_PATH)
    logger.info(f"Model saved to {MODEL_PATH}")
    logger.info(f"Encoder saved to {ENCODER_PATH}")

if __name__ == "__main__":
    train()

