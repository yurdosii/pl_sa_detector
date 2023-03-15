from enum import Enum


class PoliticalLeaningEnum(Enum):
    pro_ukrainian = "Pro-Ukrainian"
    pro_russian = "Pro-Russian"


class SentimentEnum(Enum):
    positive = "Positive"
    negative = "Negative"
    neutral = "Neutral"
