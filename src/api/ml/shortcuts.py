import pickle
from typing import cast

from sklearn.feature_extraction.text import BaseEstimator

from src.pl_sa_detector import settings

ML_PATH_PREFIX = "data/ml_models/"


def load_ml_model(model_name: str) -> tuple[BaseEstimator, BaseEstimator]:
    with open(ML_PATH_PREFIX + model_name, "rb") as file:
        model, vectorizer = pickle.load(file)
        return model, vectorizer


def predict_message_info(message: str) -> dict[str, int]:
    return {
        "political_leaning": predict_message_political_leaning(message),
        "sentiment": predict_message_sentiment(message),
    }


def predict_message_political_leaning(message: str) -> int:
    """
    0: Pro-Russian
    1: Pro-Ukrainian
    """
    return _predict(
        model=settings.ML_MODELS["PL_model"],
        vect=settings.ML_MODELS["PL_vect"],
        message=message,
    )


def predict_message_sentiment(message: str) -> int:
    """
    0: Negative
    1: Neutral
    2: Positive
    """
    return _predict(
        model=settings.ML_MODELS["SA_model"],
        vect=settings.ML_MODELS["SA_vect"],
        message=message,
    )


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
