import os

from dotenv import load_dotenv

load_dotenv(".env")


SQLALCHEMY_DATABASE_URL = os.environ.get("DATABASE_URL", "")

ML_SERVICE_URL = os.environ.get(
    "ML_SERVICE_URL",
    "http://compose_ml_service:8000",
)
