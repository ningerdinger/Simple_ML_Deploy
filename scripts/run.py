#!/usr/bin/env python
"""Script to run the API server."""
import sys
import uvicorn
from src.app import app
from src.config import API_HOST, API_PORT, LOG_LEVEL

if __name__ == "__main__":
    try:
        uvicorn.run(
            app,
            host=API_HOST,
            port=API_PORT,
            log_level=LOG_LEVEL.lower()
        )
    except Exception as e:
        print(f"Error running server: {e}")
        sys.exit(1)
