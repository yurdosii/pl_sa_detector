from contextlib import asynccontextmanager
from typing import AsyncGenerator

from fastapi import FastAPI

from src.api.ml.shortcuts import load_ml_model
from src.api.ml.views import router as ml_router
from src.api.pl_sa.views import router as pl_sa_router
from src.pl_sa_detector import settings


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
    # load ML models
    pl_model, pl_vect = load_ml_model(settings.PL_MODEL_PATH)
    settings.ML_MODELS["PL_model"] = pl_model
    settings.ML_MODELS["PL_vect"] = pl_vect

    sa_model, sa_vect = load_ml_model(settings.SA_MODEL_PATH)
    settings.ML_MODELS["SA_model"] = sa_model
    settings.ML_MODELS["SA_vect"] = sa_vect

    yield

    # clean up
    settings.ML_MODELS.clear()


app = FastAPI(title="My API", lifespan=lifespan)
app.include_router(pl_sa_router)
app.include_router(ml_router)


@app.get("/")
async def read_root() -> dict[str, str]:
    return {"Hello": "World"}
