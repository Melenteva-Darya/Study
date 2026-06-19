import os
from typing import Any
from typing import Hashable

import pandas as pd


def read_csv_file(file_path_csv: str) -> list[Any] | list[dict[Hashable, Any]]:
    """Загружает CSV-файл и возвращает список транзакций (словарей)."""
    if os.path.isfile(file_path_csv):
        final_path = file_path_csv
    else:
        current_script_dir = os.path.dirname(os.path.abspath(__file__))
        smart_dir = os.path.dirname(current_script_dir)

        # Запускаем поиск по всем папкам проекта
        for root_folder, _, files in os.walk(smart_dir):
            if file_path_csv in files:
                final_path = os.path.join(root_folder, file_path_csv)
                break
        else:
            # Этот блок сработает, только если цикл обошел всё и НЕ нашел файл
            return []

    try:
        transactions_file = pd.read_csv(final_path, encoding="utf-8")
        # Конвертируем DataFrame в список словарей и обрабатываем пустые значения (NaN) в пустые строки
        transactions_file = transactions_file.fillna("")
        return list(transactions_file.to_dict(orient="records"))

    except (FileNotFoundError, pd.errors.EmptyDataError, pd.errors.ParserError, LookupError) as e:
        print(f"Ошибка при чтении CSV-файла: {e}")
        return []


def read_excel_file(file_path_excel: str) -> list[Any] | list[dict[Hashable, Any]]:
    """Загружает Excel-файл и возвращает список транзакций (словарей)."""
    if os.path.isfile(file_path_excel):
        final_path = file_path_excel
    else:
        current_script_dir = os.path.dirname(os.path.abspath(__file__))
        smart_dir = os.path.dirname(current_script_dir)

        # Запускаем поиск по всем папкам проекта
        for root_folder, _, files in os.walk(smart_dir):
            if file_path_excel in files:
                final_path = os.path.join(root_folder, file_path_excel)
                break
        else:
            # Этот блок сработает, только если цикл обошел всё и НЕ нашел файл
            return []

    try:
        transactions_file = pd.read_excel(final_path)
        # Конвертируем DataFrame в список словарей и обрабатываем пустые значения (NaN) в пустые строки
        transactions_file = transactions_file.fillna("")
        return list(transactions_file.to_dict(orient="records"))

    except (FileNotFoundError, ValueError, TypeError, ImportError) as e:
        print(f"Ошибка при чтении Excel-файла: {e}")
        return []
