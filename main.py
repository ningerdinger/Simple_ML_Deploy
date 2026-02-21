"""Main entry point for the Iris Classifier API."""
if __name__ == "__main__":
    import uvicorn
    from src.app import app
    from src.config import API_HOST, API_PORT, LOG_LEVEL

    uvicorn.run(
        app,
        host=API_HOST,
        port=API_PORT,
        log_level=LOG_LEVEL.lower()
    )
