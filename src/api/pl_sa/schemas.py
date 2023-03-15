from pydantic import BaseModel

from .enums import PoliticalLeaningEnum, SentimentEnum


class Info(BaseModel):
    political_leaning: PoliticalLeaningEnum
    sentiment: SentimentEnum
