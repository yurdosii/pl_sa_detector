from .enums import PoliticalLeaningEnum, SentimentEnum
from .schemas import Info


def get_message_info(message: str) -> Info:
    return Info(
        political_leaning=get_message_political_leaning(message),
        sentiment=get_message_sentiment(message),
    )


def get_message_political_leaning(message: str) -> PoliticalLeaningEnum:
    return PoliticalLeaningEnum.pro_ukrainian


def get_message_sentiment(message: str) -> SentimentEnum:
    return SentimentEnum.neutral
