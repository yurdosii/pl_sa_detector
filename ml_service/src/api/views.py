from fastapi import APIRouter

from .shortcuts import (
    predict_message_info,
    predict_message_political_leaning,
    predict_message_sentiment,
)

router = APIRouter(prefix="/ml", tags=["Machine Learning"])


@router.get("/predict")
async def predict_info(message: str) -> dict[str, str]:
    return predict_message_info(message)


@router.get("/predict_pl")
async def predict_political_leaning(message: str) -> dict[str, str]:
    return predict_message_political_leaning(message)


@router.get("/predict_sa")
async def predict_sentiment(message: str) -> dict[str, str]:
    return predict_message_sentiment(message)
