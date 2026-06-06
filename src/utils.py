import os
import json
from json import JSONDecodeError
from typing import Union

script_dir = os.path.dirname(os.path.abspath(__file__))
path_to_file = os.path.abspath(os.path.join(script_dir, '..', 'data', 'operations.json'))

def get_financial_transactions(file_path: str) -> Union[list, str]:
    """Читает JSON-файл и возвращает список словарей с финансовыми транзакциями.
       Если файл не найден, пуст или содержит не список — возвращает []."""
    try:
        if not file_path:
            return []
        if not os.path.exists(file_path):
            return []
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            if isinstance(data, list):
                return data
            return []
    except (JSONDecodeError, PermissionError, FileNotFoundError):
        return []
