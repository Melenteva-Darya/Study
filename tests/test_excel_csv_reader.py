from typing import Any
from unittest.mock import patch

import pandas as pd

from src.excel_csv_reader import read_csv_file
from src.excel_csv_reader import read_excel_file


@patch("src.excel_csv_reader.os.path.isfile")
def test_read_csv_file_not_found(mock_file: Any) -> None:
    """Тест: файл не существует"""
    mock_file.return_value = False
    result = read_csv_file("transaction.csv")

    assert isinstance(result, pd.DataFrame)
    assert result.empty


@patch("src.excel_csv_reader.pd.read_csv")
@patch("src.excel_csv_reader.os.path.isfile")
def test_read_csv_file_success(mock_file: Any, mock_read_csv: Any) -> None:
    """Тест: успешное чтение корректного CSV-файла с одним аргументом"""
    mock_file.return_value = True
    fake_df = pd.DataFrame([{"id": 123, "amount": 100}])
    mock_read_csv.return_value = fake_df
    result = read_csv_file("transactions.csv")

    assert isinstance(result, pd.DataFrame)
    assert result.to_dict(orient="records") == [{"id": 123, "amount": 100}]


@patch("src.excel_csv_reader.pd.read_csv")
@patch("src.excel_csv_reader.os.path.isfile")
def test_read_csv_file_parser_error(mock_isfile: Any, mock_read_csv: Any) -> None:
    """Тест: файл CSV сломан или поврежден (ParserError)"""
    mock_isfile.return_value = True
    # Заставляем pandas выкинуть ошибку
    mock_read_csv.side_effect = pd.errors.ParserError("Ошибка структуры CSV")

    result = read_csv_file("bad_transactions.csv")

    # Код должен перехватить ошибку и вернуть пустой DataFrame
    assert isinstance(result, pd.DataFrame)
    assert result.empty


@patch("src.excel_csv_reader.pd.read_excel")
@patch("src.excel_csv_reader.os.path.isfile")
def test_read_excel_file_type_error(mock_isfile: Any, mock_read_excel: Any) -> None:
    """Тест: ошибка типа данных при чтении Excel (TypeError)"""
    mock_isfile.return_value = True
    mock_read_excel.side_effect = TypeError("Неверный тип данных в ячейках")

    result = read_excel_file("bad_transactions.xlsx")

    assert isinstance(result, pd.DataFrame)
    assert result.empty


@patch("src.excel_csv_reader.os.path.isfile")
def test_read_excel_file_not_found(mock_file: Any) -> None:
    """Тест: файл не существует"""
    mock_file.return_value = False
    result = read_excel_file("transaction.xlsx")

    assert isinstance(result, pd.DataFrame)
    assert result.empty


@patch("src.excel_csv_reader.pd.read_excel")
@patch("src.excel_csv_reader.os.path.isfile")
def test_read_excel_file_success(mock_isfile: Any, mock_read_excel: Any) -> None:
    """Тест: успешное чтение корректного Excel-файла с одним аргументом"""
    mock_isfile.return_value = True
    fake_df = pd.DataFrame([{"id": 123, "amount": 100}])
    mock_read_excel.return_value = fake_df
    result = read_excel_file("transactions.xlsx")

    assert isinstance(result, pd.DataFrame)
    assert result.to_dict(orient="records") == [{"id": 123, "amount": 100}]


@patch("src.excel_csv_reader.pd.read_csv")
@patch("src.excel_csv_reader.os.walk")
@patch("src.excel_csv_reader.os.path.isfile")
def test_read_csv_file_smart_search_success(mock_isfile: Any, mock_walk: Any, mock_read_csv: Any) -> None:
    """Тест: файла нет по прямому пути, но "smart" поиск нашел его в подпапке"""
    mock_isfile.return_value = False  # Прямой путь не найден

    # Имитируем, что os.walk нашел наш файл 'transactions.csv' в папке 'data'
    # os.walk возвращает кортеж (путь_к_папке, [подпапки], [файлы])
    mock_walk.return_value = [("/project/data", [], ["transactions.csv"])]

    fake_df = pd.DataFrame([{"id": 999}])
    mock_read_csv.return_value = fake_df

    result = read_csv_file("transactions.csv")

    # Проверяем, что smart-поиск отработал и вернул данные найденного файла
    assert result.to_dict(orient="records") == [{"id": 999}]
