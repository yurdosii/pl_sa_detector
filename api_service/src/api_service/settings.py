import os
from dotenv import load_dotenv

STAGE = os.environ.get("STAGE", "dev")

if STAGE == "dev":
    load_dotenv(".env")


SQLALCHEMY_DATABASE_URL = os.environ.get("DATABASE_URL", "")

ML_SERVICE_URL = os.environ.get(
    "ML_SERVICE_URL",
    "http://compose_ml_service:8000",
)
