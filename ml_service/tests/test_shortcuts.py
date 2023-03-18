import pytest

from src.api.shortcuts import (
    predict_message_info,
    predict_message_political_leaning,
    predict_message_sentiment,
)


@pytest.mark.parametrize(
    "message, expected",
    [
        (
            "Україна",
            {"political_leaning": "pro_ukrainian", "sentiment": "positive"},
        ),
        (
            "Війна",
            {"political_leaning": "pro_ukrainian", "sentiment": "negative"},
        ),
    ],
)
def test_predict_message_info(
    setup_models,
    message,
    expected,
):
    assert predict_message_info(message) == expected


@pytest.mark.parametrize(
    "message, expected",
    [
        (
            "Glory to Ukraine",
            {"political_leaning": "pro_ukrainian"},
        ),
        (
            "Мариуполь",
            {"political_leaning": "pro_russian"},
        ),
    ],
)
def test_predict_message_political_leaning(
    setup_models,
    message,
    expected,
):
    assert predict_message_political_leaning(message) == expected


@pytest.mark.parametrize(
    "message, expected",
    [
        (
            "Україна",
            {"sentiment": "positive"},
        ),
        (
            "Незабаром літо",
            {"sentiment": "neutral"},
        ),
        (
            "Ракети удар смерть",
            {"sentiment": "negative"},
        ),
    ],
)
def test_predict_message_sentiment(
    setup_models,
    message,
    expected,
):
    assert predict_message_sentiment(message) == expected
