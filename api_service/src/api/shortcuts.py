from .service import call_ml_service


def get_message_info(message: str) -> dict[str, str]:
    return call_ml_service("/ml/predict", message)


def get_message_political_leaning(message: str) -> dict[str, str]:
    return call_ml_service("/ml/predict_pl", message)


def get_message_sentiment(message: str) -> dict[str, str]:
    return call_ml_service("/ml/predict_sa", message)
