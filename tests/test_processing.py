import pytest
from src.processing import filter_by_state, sort_by_date


@pytest.mark.parametrize("state_argument, output_function",
                         [('EXECUTED', [{'id': 414288290, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                                        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]),
                          ('CANCELED', [{'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
                                        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]),
                          ('PENDING', []),
                          ])
def test_filter(input_argument_list, state_argument, output_function):
    assert filter_by_state(input_argument_list, state_argument) == output_function


def test_filter_empty():
    input_argument_list = []
    state_argument = 'CANCELED'
    output_function = "Ошибка: список пуст!"

    assert filter_by_state(input_argument_list, state_argument) == output_function


def test_filter_empty_state(input_argument_list):

    state_argument = ""
    output_function = [{'id': 414288290, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
                       {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'}]

    assert filter_by_state(input_argument_list, state_argument) == output_function
