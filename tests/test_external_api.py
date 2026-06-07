from typing import Any
from unittest.mock import patch

from src.external_api import currency_conversion


@patch("src.external_api.requests.get")
def test_currency_conversion(mock_get: Any) -> None:
    """Тест: успешная конвертация USD в RUB с подменой ответа сервера (без интернета)"""
    mock_get.return_value.json.return_value = {"Valute": {"USD": {"Value": 73.4689}}}

    transaction_1 = [{"operationAmount": {"amount": "150.00", "currency": {"code": "USD"}}}]

    result = currency_conversion(transaction_1)
    assert result == 11020.34


@patch("src.external_api.requests.get")
def test_currency_conversion_eur(mock_get: Any) -> None:
    """Тест: успешная конвертация USD в RUB с подменой ответа сервера (без интернета)"""
    mock_get.return_value.json.return_value = {"Valute": {"EUR": {"Value": 85.5582}}}

    transaction_1 = [{"operationAmount": {"amount": "150.00", "currency": {"code": "EUR"}}}]

    result = currency_conversion(transaction_1)
    assert result == 12833.73


def test_currency_conversion_rub() -> None:
    """Тест рублевой транзакции: без моков, патчей и интернета"""

    transaction_rub = [{"operationAmount": {"amount": "1500.50", "currency": {"code": "RUB"}}}]

    result = currency_conversion(transaction_rub)

    assert result == 1500.50
