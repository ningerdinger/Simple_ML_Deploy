# Use a lightweight Python base image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install system dependencies (optional but often needed for sklearn)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Install uv
RUN pip install uv

# Copy pyproject.toml and uv.lock (better caching)
COPY pyproject.toml uv.lock ./

# Create virtual environment and install Python dependencies with uv
RUN uv venv && uv pip install --system -r pyproject.toml

# Copy application code, scripts, and data
COPY src ./src
COPY main.py .
COPY data ./data
COPY iris_model.joblib label_encoder.joblib ./

# Copy .env.example for reference
COPY .env.example .

# Expose FastAPI port
EXPOSE 8000

# Start the API server
CMD ["python", "main.py"]
