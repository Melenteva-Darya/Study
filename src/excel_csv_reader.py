import os
from typing import Any

import pandas as pd
from pandas import DataFrame


def read_csv_file(file_path_csv: str) -> DataFrame | list[Any]:
    """Загружает CSV-файл в Pandas DataFrame.
    Принимает как полный абсолютный путь, так и просто имя файла."""
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
            return pd.DataFrame()

    try:
        transactions_file = pd.read_csv(final_path, encoding="utf-8")
        return transactions_file

    except (FileNotFoundError, pd.errors.EmptyDataError, pd.errors.ParserError, LookupError) as e:
        print(f"Ошибка при чтении CSV-файла: {e}")
        return pd.DataFrame()


def read_excel_file(file_path_excel: str) -> DataFrame:
    """Загружает Exel-файл в Pandas DataFrame.
    Принимает как полный абсолютный путь, так и просто имя файла."""
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
            return pd.DataFrame()

    try:
        transactions_file = pd.read_excel(final_path)
        return transactions_file

    except (FileNotFoundError, ValueError, TypeError, ImportError) as e:
        print(f"Ошибка при чтении Excel-файла: {e}")
        return pd.DataFrame()
