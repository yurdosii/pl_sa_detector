from fastapi import APIRouter

from .enums import PoliticalLeaningEnum, SentimentEnum
from .schemas import Info
from .shortcuts import (
    get_message_info,
    get_message_political_leaning,
    get_message_sentiment,
)

router = APIRouter(prefix="/message", tags=["message"])


@router.post("/get")
async def get_info(message: str) -> Info:
    """
    Get political leaning and sentiment of the message
    """
    return get_message_info(message)


@router.post("/get_pl")
async def get_political_leaning(message: str) -> PoliticalLeaningEnum:
    """
    Get political leaning of the message (Pro-Ukrainian or Pro-Russian)
    """
    return get_message_political_leaning(message)


@router.post("/get_sa")
async def get_sentiment(message: str) -> SentimentEnum:
    """
    Get sentiment of the message (Negative, Neutral or Positive)
    """
    return get_message_sentiment(message)
