import pickle
from typing import cast

from sklearn.feature_extraction.text import BaseEstimator

from ..ml_service import settings
from .enums import PoliticalLeaningEnum, SentimentEnum

ML_PATH_PREFIX: str = "data/ml_models/"


def load_ml_model(model_name: str) -> tuple[BaseEstimator, BaseEstimator]:
    with open(ML_PATH_PREFIX + model_name, "rb") as file:
        model, vectorizer = pickle.load(file)
        return model, vectorizer


def predict_message_info(message: str) -> dict[str, str]:
    return {
        "political_leaning": _predict_message_political_leaning(message),
        "sentiment": _predict_message_sentiment(message),
    }


def predict_message_political_leaning(message: str) -> dict[str, str]:
    """
    0: Pro-Russian
    1: Pro-Ukrainian
    """
    result = _predict_message_political_leaning(message)
    return {"political_leaning": result}


def _predict_message_political_leaning(message: str) -> str:
    value = _predict(
        model=settings.ML_MODELS["PL_model"],
        vect=settings.ML_MODELS["PL_vect"],
        message=message,
    )
    return PoliticalLeaningEnum(value).name


def predict_message_sentiment(message: str) -> dict[str, str]:
    """
    0: Negative
    1: Neutral
    2: Positive
    """
    result = _predict_message_sentiment(message)
    return {"sentiment": result}


def _predict_message_sentiment(message: str) -> str:
    value = _predict(
        model=settings.ML_MODELS["SA_model"],
        vect=settings.ML_MODELS["SA_vect"],
        message=message,
    )
    return SentimentEnum(value).name


def _predict(
    *,
    model: BaseEstimator,
    vect: BaseEstimator,
    message: str,
) -> int:
    vect_message = vect.transform([message])
    result = cast(int, model.predict(vect_message)[0])
    return result


if __name__ == "__main__":
    # load model
    file = open("data/ml_models/sa_model.pkl", "rb")
    model, vectorizer = pickle.load(file)  # LinearSVC, TfidfVectorizer

    # predict
    text = "Слава Україні"
    #  <1x237546 sparse matrix of type '<class 'numpy.float64'>'
    # with 0 stored elements in Compressed Sparse Row format>
    vect_text = vectorizer.transform([text])
    model.predict(vect_text)  # array([1])
