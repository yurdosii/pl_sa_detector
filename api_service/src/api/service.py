from typing import cast

import httpx

from src.api_service.settings import ML_SERVICE_URL


def call_ml_service(endpoint_path: str, message: str) -> dict[str, str]:
    """
    Docker containers are in the same network and can be accessed
    via a docker container name as a hostname:

    `docker-compose up --build`
    `docker-compose exec compose_api_service python`

    >>> import httpx
    >>> httpx.get("http://compose_api_service:8000/").json()
    {'Hello': 'API World'}
    >>> httpx.get("http://compose_ml_service:8000/").json()
    {'Hello': 'ML World'}
    """

    url = ML_SERVICE_URL + endpoint_path
    params = {"message": message}
    result = cast(dict[str, str], httpx.get(url, params=params).json())
    return result
