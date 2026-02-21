import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier

# Load dataset
df = pd.read_csv("iris.csv")
df = df.drop(columns=["Id"])

# Split features/labels
X = df.drop("Species", axis=1)
y = df["Species"]

# Encode labels
le = LabelEncoder()
y_encoded = le.fit_transform(y)

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y_encoded, test_size=0.2, random_state=42
)

# Train model
model = RandomForestClassifier(n_estimators=200, random_state=42)
model.fit(X_train, y_train)

# Save artifacts
joblib.dump(model, "iris_model.joblib")
joblib.dump(le, "label_encoder.joblib")

print("Model and label encoder saved.")
