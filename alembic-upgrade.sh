#!/bin/bash



set -e

# Run Alembic upgrade
alembic upgrade head

# Start FastAPI app after migration (if needed)
uvicorn app.main:app --host 0.0.0.0 --port 8000