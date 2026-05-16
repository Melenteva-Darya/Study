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
