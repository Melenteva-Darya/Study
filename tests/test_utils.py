from unittest.mock import patch, mock_open, Mock

from src.utils import get_financial_transactions


@patch('os.path.exists')
def test_get_transactions_file_not_found(self, mock_exists):
    """Тест открытия: файл не существует на диске"""
    mock_exists.return_value = False
    result = get_financial_transactions('fake.json')
    self.assertEqual(result, [])


@patch('os.path.exists')
def test_get_transactions_success(self, mock_exists):
    """Тест открытия: успешное чтение корректного JSON-списка"""
    mock_exists.return_value = True
    fake_json = '[{"id": 123, "amount": 100}]'

    with patch('builtins.open', mock_open(read_data=fake_json)):
        result = get_financial_transactions('fake.json')

    self.assertEqual(result, [{"id": 123, "amount": 100}])
