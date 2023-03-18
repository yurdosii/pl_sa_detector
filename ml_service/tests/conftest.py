import pytest

from src.api.shortcuts import load_ml_model
from src.ml_service import settings


@pytest.fixture(scope="session")
def setup_models():
    pl_model, pl_vect = load_ml_model(settings.PL_MODEL_PATH)
    settings.ML_MODELS["PL_model"] = pl_model
    settings.ML_MODELS["PL_vect"] = pl_vect

    sa_model, sa_vect = load_ml_model(settings.SA_MODEL_PATH)
    settings.ML_MODELS["SA_model"] = sa_model
    settings.ML_MODELS["SA_vect"] = sa_vect
