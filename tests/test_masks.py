from typing import Any

from src.masks import get_mask_account, get_mask_card_number


def test_mask_card_1(card_1: Any) -> None:
    assert get_mask_card_number("1234123412341234") == card_1


def test_mask_card_2(card_empty_line: Any) -> None:
    assert get_mask_card_number("") == card_empty_line


def test_mask_card_3(card_more_or_less: Any) -> None:
    assert get_mask_card_number("6578952546713") == card_more_or_less


def test_mask_card_4(card_more_or_less: Any) -> None:
    assert get_mask_card_number("65789525467136254154") == card_more_or_less


def test_mask_account_1(account_1: Any) -> None:
    assert get_mask_account("12341234123412341234") == account_1


def test_mask_account_2(account_empty_line: Any) -> None:
    assert get_mask_account("") == account_empty_line


def test_mask_account_3(account_more_or_less: Any) -> None:
    assert get_mask_account("657895254671545365") == account_more_or_less


def test_mask_account_4(account_more_or_less: Any) -> None:
    assert get_mask_account("65789525467154536241415") == account_more_or_less
