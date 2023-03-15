from fastapi import APIRouter
from pydantic import BaseModel

from .enums import PoliticalLeaningEnum, SentimentEnum
from .shortcuts import get_msg_political_leaning, get_msg_sentiment

router = APIRouter(prefix="/message", tags=["message"])


class Info(BaseModel):
    political_leaning: PoliticalLeaningEnum
    sentiment: SentimentEnum


@router.post("/get_pl")
async def get_political_leaning(message: str) -> PoliticalLeaningEnum:
    """
    Get political leaning of the message (Pro-Ukrainian or Pro-Russian)
    """
    return get_msg_political_leaning(message)


@router.post("/get_sa")
async def get_sentiment(message: str) -> SentimentEnum:
    """
    Get sentiment of the message (Positive, Neutral or Negative)
    """
    return get_msg_sentiment(message)


@router.post("/get_info")
async def get_info(message: str) -> Info:
    """
    Get political leaning and sentiment of the message
    """
    return Info(
        political_leaning=get_msg_political_leaning(message),
        sentiment=get_msg_sentiment(message),
    )
