from typing import Any

import pytest

from src.generators import card_number_generator
from src.generators import filter_by_currency
from src.generators import transaction_descriptions


@pytest.mark.parametrize(
    "target_currency, expected_transactions",
    [
        (
            "USD",
            [
                {
                    "id": 939719570,
                    "state": "EXECUTED",
                    "date": "2018-06-30T02:08:58.425572",
                    "operationAmount": {
                        "amount": "9824.07",
                        "currency": {"name": "USD", "code": "USD"},
                    },
                    "description": "Перевод организации",
                    "from": "Счет 75106830613657916952",
                    "to": "Счет 11776614605963066702",
                },
                {
                    "id": 142264268,
                    "state": "EXECUTED",
                    "date": "2019-04-04T23:20:05.206878",
                    "operationAmount": {
                        "amount": "79114.93",
                        "currency": {"name": "USD", "code": "USD"},
                    },
                    "description": "Перевод со счета на счет",
                    "from": "Счет 19708645243227258542",
                    "to": "Счет 75651667383060284188",
                },
                {
                    "id": 895315941,
                    "state": "EXECUTED",
                    "date": "2018-08-19T04:27:37.904916",
                    "operationAmount": {
                        "amount": "56883.54",
                        "currency": {"code": "USD", "name": "USD"},
                    },
                    "description": "Перевод с карты на карту",
                    "from": "Visa Classic 6831982476737658",
                    "to": "Visa Platinum 8990922113665229",
                },
            ],
        ),
        (
            "EUR",
            [],
        ),
    ],
)
def test_filter_by_currency_full_data(
    sample_transactions: list[dict[str, Any]],
    target_currency: str,
    expected_transactions: list[dict[str, Any]],
) -> None:
    """Проверяет фильтрацию по валюте и отсутствие совпадений."""
    usd_transactions = filter_by_currency(sample_transactions, target_currency)
    actual_transactions = list(usd_transactions)

    assert actual_transactions == expected_transactions


@pytest.mark.parametrize(
    "invalid_input",
    [
        [],
        [{"id": 123, "description": "Транзакция без блока operationAmount"}],
    ],
)
def test_filter_by_currency_empty_and_corrupted_data(invalid_input: list[dict[str, Any]]) -> None:
    """Пустой список или списка без валютной операции."""
    result_iterator = filter_by_currency(invalid_input, "USD")
    result_list = list(result_iterator)

    assert result_list == []


def test_transaction_descriptions_correct_yield(sample_transactions: list[dict[str, Any]]) -> None:
    """Генератор поочередно выдает описания каждой операции."""
    descriptions = transaction_descriptions(sample_transactions)

    assert next(descriptions) == "Перевод организации"
    assert next(descriptions) == "Перевод со счета на счет"
    assert next(descriptions) == "Перевод со счета на счет"
    assert next(descriptions) == "Перевод с карты на карту"
    assert next(descriptions) == "Перевод организации"


def test_transaction_descriptions_empty_list() -> None:
    """Проверяет с пустым списком."""
    descriptions = transaction_descriptions([])

    with pytest.raises(StopIteration):
        next(descriptions)


def test_transaction_descriptions_missing_key() -> None:
    """Проверяет, что код не падает, если у транзакции нет ключа 'description'."""
    corrupted_data = [{"id": 111}]
    descriptions = transaction_descriptions(corrupted_data)

    assert next(descriptions) == ""


@pytest.mark.parametrize(
    "start, stop, expected_list",
    [
        (
            1,
            3,
            [
                "0000 0000 0000 0001",
                "0000 0000 0000 0002",
                "0000 0000 0000 0003",
            ],
        ),
        (99, 99, ["0000 0000 0000 0099"]),
        (9, 11, ["0000 0000 0000 0009", "0000 0000 0000 0010", "0000 0000 0000 0011"]),
    ],
)
def test_card_number_generator_correct_output(start: int, stop: int, expected_list: list[str]) -> None:
    """Проверяет, что генератор выдает правильные номера в заданном диапазоне
    и корректно форматирует их (пробелы и нули).
    """
    result_generator = card_number_generator(start, stop)
    actual_list = list(result_generator)

    assert actual_list == expected_list


def test_card_number_generator_stops_correctly() -> None:
    """Убеждается, что генератор правильно завершает генерацию (вызывает StopIteration)
    после выдачи последнего элемента диапазона."""
    generator = card_number_generator(1, 2)

    assert next(generator) == "0000 0000 0000 0001"
    assert next(generator) == "0000 0000 0000 0002"

    with pytest.raises(StopIteration):
        next(generator)


def test_card_number_generator_invalid_range() -> None:
    """Проверяет поведение генератора, если начальное значение больше конечного."""
    generator = card_number_generator(5, 1)

    assert list(generator) == []
