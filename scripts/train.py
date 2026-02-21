#!/usr/bin/env python
"""Training script for the Iris Classifier model."""
import sys
from src.train_model import train

if __name__ == "__main__":
    try:
        train()
    except Exception as e:
        print(f"Error during training: {e}")
        sys.exit(1)
