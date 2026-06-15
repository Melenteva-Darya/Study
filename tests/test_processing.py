from typing import Any

import pytest

from src.processing import filter_by_state
from src.processing import sort_by_date


@pytest.mark.parametrize(
    "state_argument, output_function",
    [
        (
            "EXECUTED",
            [
                {"id": 414288290, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            ],
        ),
        (
            "CANCELED",
            [
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
            ],
        ),
        ("PENDING", []),
    ],
)
def test_filter(input_argument_list: Any, state_argument: Any, output_function: Any) -> None:
    assert filter_by_state(input_argument_list, state_argument) == output_function


def test_filter_empty() -> None:
    input_argument_list: list[dict[str, Any]] = []
    state_argument: str = "CANCELED"
    output_function: str = "Ошибка: список пуст!"

    assert filter_by_state(input_argument_list, state_argument) == output_function


def test_filter_empty_state(input_argument_list: list[dict[str, Any]]) -> None:
    state_argument: str = ""
    output_function: list[dict[str, Any]] = [
        {"id": 414288290, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]

    assert filter_by_state(input_argument_list, state_argument) == output_function


@pytest.mark.parametrize(
    "reverse_argument, output_function",
    [
        (
            True,
            [
                {"id": 414288290, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            ],
        ),
        (
            False,
            [
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
                {"id": 414288290, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
            ],
        ),
        (
            "",
            [
                {"id": 414288290, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
                {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
                {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
                {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
            ],
        ),
    ],
)
def test_sort(input_argument_list: Any, reverse_argument: Any, output_function: Any) -> None:
    assert sort_by_date(input_argument_list, reverse_argument) == output_function


def test_sort_identical_dates() -> None:
    input_argument_list = [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-06-30T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]
    reverse_argument = True
    output_function = [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-06-30T21:27:25.241689"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]

    assert sort_by_date(input_argument_list, reverse_argument) == output_function


def test_sort_incorrect_format() -> None:
    input_argument_list = [
        {"id": 594226727, "state": "CANCELED", "date": "неверный формат"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]
    reverse_argument = True
    output_function = "Ошибка: неверный формат даты в списке!"

    assert sort_by_date(input_argument_list, reverse_argument) == output_function


def test_sort_incorrect_format_1() -> None:
    input_argument_list = [
        {
            "id": 594226727,
            "state": "CANCELED",
        },
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    ]
    reverse_argument = True
    output_function = "Ошибка: неверный формат даты в списке!"

    assert sort_by_date(input_argument_list, reverse_argument) == output_function
