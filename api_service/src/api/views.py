from fastapi import APIRouter

from .shortcuts import (
    get_message_info,
    get_message_political_leaning,
    get_message_sentiment,
)

router = APIRouter(prefix="/message", tags=["message"])


@router.get("/get")
async def get_info(message: str) -> dict[str, str]:
    """
    Get political leaning and sentiment of the message
    """
    return get_message_info(message)


@router.get("/get_pl")
async def get_political_leaning(message: str) -> dict[str, str]:
    """
    Get political leaning of the message (Pro-Ukrainian or Pro-Russian)
    """
    return get_message_political_leaning(message)


@router.get("/get_sa")
async def get_sentiment(message: str) -> dict[str, str]:
    """
    Get sentiment of the message (Negative, Neutral or Positive)
    """
    return get_message_sentiment(message)
