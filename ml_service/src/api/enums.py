from enum import Enum


class PoliticalLeaningEnum(Enum):
    pro_russian = 0  # "Pro-Russian"
    pro_ukrainian = 1  # "Pro-Ukrainian"


class SentimentEnum(Enum):
    negative = 0  # "Negative"
    neutral = 1  # "Neutral"
    positive = 2  # "Positive"
