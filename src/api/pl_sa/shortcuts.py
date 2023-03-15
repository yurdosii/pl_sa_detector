from .enums import PoliticalLeaningEnum, SentimentEnum


def get_msg_political_leaning(msg: str) -> PoliticalLeaningEnum:
    return PoliticalLeaningEnum.pro_ukrainian


def get_msg_sentiment(msg: str) -> SentimentEnum:
    return SentimentEnum.neutral
