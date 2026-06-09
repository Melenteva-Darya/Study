import json
import logging
import os
from json import JSONDecodeError
from typing import Any, Union

script_dir = os.path.dirname(os.path.abspath(__file__))
path_to_file = os.path.abspath(os.path.join(script_dir, "..", "data", "operations.json"))

log_dir = os.path.abspath(os.path.join(script_dir, "..", "logs"))
log_file_path = os.path.join(log_dir, "utils.log")


utils_logger = logging.getLogger(__name__)
utils_logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler(log_file_path, mode="w", encoding="utf-8")

file_formatter = logging.Formatter("%(asctime)s %(filename)s %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)

utils_logger.addHandler(file_handler)
utils_logger.debug("Debug message")


def get_financial_transactions(file_path: str) -> Union[list[Any], str]:
    """Читает JSON-файл и возвращает список словарей с финансовыми транзакциями.
    Если файл не найден, пуст или содержит не список — возвращает []."""
    try:
        if not file_path:
            utils_logger.warning("Путь к файлу не указан")
            return []

        if not os.path.exists(file_path):
            utils_logger.warning("Файл не найден")
            return []

        utils_logger.info(f"Начало чтения данных из файла: {file_path}")

        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            if isinstance(data, list):
                utils_logger.info(f"Данные успешно прочитаны. Найдено транзакций: {len(data)}")
                return data
            return []
    except (JSONDecodeError, PermissionError, FileNotFoundError) as e:
        utils_logger.error(f"Произошла ошибка: {e}", exc_info=True)
        return []
