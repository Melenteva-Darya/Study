import pytest
from src.widget import mask_account_card, get_date


@pytest.mark.parametrize("input_argument, output_function",
                         [("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
                          ("Счет 73654108430135874305", "Счет **4305"),
                          ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
                          ("Счет 64686473678894779589", "Счет **9589"),
                          ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
                          ("Счет 35383033474447895560", "Счет **5560"),
                          ("Visa Classic 6831982476737658", "Visa Classic 6831 98** **** 7658"),
                          ("Visa Platinum 8990922113665229", "Visa Platinum 8990 92** **** 5229"),
                          ("Visa Gold 5999414228426353", "Visa Gold 5999 41** **** 6353"),
                          ("Счет 73654108430135874305", "Счет **4305"), ])
def test_mask_1(input_argument, output_function):
    assert mask_account_card(input_argument) == output_function


def test_mask_2(card_empty_line):
    assert mask_account_card("") == card_empty_line


def test_mask_3():
    assert mask_account_card("6578952546713") == "Ошибка: неверное количество цифр (нужно 16 или 20)!"


def test_mask_4():
    assert mask_account_card("65789525467136254154456") == "Ошибка: неверное количество цифр (нужно 16 или 20)!"


def test_mask_5():
    assert mask_account_card("Visa #@g") == "Ошибка: строка содержит недопустимые символы!"


@pytest.mark.parametrize("input_argument, output_function",
                         [("2024-03-11T02:26:18.671407", "11.03.2024"),
                          ("  2024-03-12T02:26:18.671407  ", "12.03.2024"),
                          ("Перевод организации 2024-03-13T02:26:18.671407", "13.03.2024"),
                          ("", "Ошибка: пустая строка!"),
                          ("2024-03-11-T02:26:18.671407", "Ошибка: неверный формат даты!"),
                          ("20224-03-11-T02:26:18.671407", "Ошибка: неверный формат даты!"),
                          ])
def test_data_1(input_argument, output_function):
    assert get_date(input_argument) == output_function
