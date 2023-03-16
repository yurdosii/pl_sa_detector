from fastapi import APIRouter

from .shortcuts import (
    predict_message_info,
    predict_message_political_leaning,
    predict_message_sentiment,
)

router = APIRouter(prefix="/ml", tags=["Machine Learning"])


@router.post("/predict")
async def predict_info(message: str) -> dict[str, int]:
    return predict_message_info(message)


@router.post("/predict_pl")
async def predict_political_leaning(message: str) -> int:
    return predict_message_political_leaning(message)


@router.post("/predict_sa")
async def predict_sentiment(message: str) -> int:
    return predict_message_sentiment(message)
