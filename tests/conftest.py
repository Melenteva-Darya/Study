import pytest

@pytest.fixture
def card_1():
    return "1234 12** **** 1234"

@pytest.fixture
def card_empty_line():
    return "Ошибка: пустая строка!"

@pytest.fixture
def card_more_or_less():
    return "Ошибка: неверное количество цифр (нужно 16)!"

@pytest.fixture
def account_1():
    return "**1234"

@pytest.fixture
def account_empty_line():
    return "Ошибка: пустая строка!"

@pytest.fixture
def account_more_or_less():
    return "Ошибка: неверное количество цифр (нужно 20)!"

@pytest.fixture
def input_argument_list():
    return [
        {'id': 414288290, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}, ]
