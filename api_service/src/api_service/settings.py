import os

ML_SERVICE_URL = os.environ.get(
    "ML_SERVICE_URL",
    "http://compose_ml_service:8000",
)
