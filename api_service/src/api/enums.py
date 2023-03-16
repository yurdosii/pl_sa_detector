from enum import Enum


class PoliticalLeaningEnum(Enum):
    pro_russian = "Pro-Russian"
    pro_ukrainian = "Pro-Ukrainian"


class SentimentEnum(Enum):
    negative = "Negative"
    neutral = "Neutral"
    positive = "Positive"
