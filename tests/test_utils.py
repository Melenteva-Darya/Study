from typing import Any
from unittest.mock import mock_open, patch

from src.utils import get_financial_transactions


@patch("utils.os.path.exists")
def test_get_transactions_file_not_found(mock_file: Any) -> None:
    """Тест: файл не существует на диске"""
    mock_file.return_value = False
    result = get_financial_transactions("fake.json")

    assert result == []


@patch("builtins.open", new_callable=mock_open, read_data='[{"id": 123, "amount": 100}]')
@patch("utils.os.path.exists")
def test_get_transactions_success(mock_exists: Any) -> None:
    """Тест: успешное чтение корректного JSON-списка"""

    mock_exists.return_value = True
    result = get_financial_transactions("fake.json")

    assert result == [{"id": 123, "amount": 100}]
