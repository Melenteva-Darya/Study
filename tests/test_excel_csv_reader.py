from typing import Any
from unittest.mock import patch

import pandas as pd

from src.excel_csv_reader import read_csv_file
from src.excel_csv_reader import read_excel_file


@patch("src.excel_csv_reader.os.path.isfile")
def test_read_csv_file_not_found(mock_file: Any) -> None:
    """Тест: файл не существует, должен вернуться пустой список"""
    mock_file.return_value = False
    result = read_csv_file("transaction.csv")

    # Проверяем, что теперь возвращается именно список
    assert isinstance(result, list)
    # Проверяем, что список пустой (без использования .empty)
    assert len(result) == 0


@patch("src.excel_csv_reader.pd.read_csv")
@patch("src.excel_csv_reader.os.path.isfile")
def test_read_csv_file_success(mock_file: Any, mock_read_csv: Any) -> None:
    """Тест: успешное чтение корректного CSV-файла"""
    mock_file.return_value = True

    # Создаем фейковый DataFrame, который вернет pd.read_csv внутри функции
    fake_df = pd.DataFrame([{"id": 123, "amount": 100}])
    mock_read_csv.return_value = fake_df

    result = read_csv_file("transactions.csv")

    # Проверяем, что на выходе получили обычный список, а не DataFrame
    assert isinstance(result, list)
    # Сравниваем полученный результат напрямую со списком словарей
    assert result == [{"id": 123, "amount": 100}]


@patch("src.excel_csv_reader.pd.read_csv")
@patch("src.excel_csv_reader.os.path.isfile")
def test_read_csv_file_parser_error(mock_isfile: Any, mock_read_csv: Any) -> None:
    """Тест: файл CSV сломан или поврежден (ParserError)"""
    mock_isfile.return_value = True
    # Заставляем pandas выкинуть ошибку
    mock_read_csv.side_effect = pd.errors.ParserError("Ошибка структуры CSV")

    result = read_csv_file("bad_transactions.csv")

    # Код должен перехватить ошибку и вернуть пустой список
    assert isinstance(result, list)
    assert len(result) == 0


@patch("src.excel_csv_reader.pd.read_excel")
@patch("src.excel_csv_reader.os.path.isfile")
def test_read_excel_file_type_error(mock_isfile: Any, mock_read_excel: Any) -> None:
    """Тест: ошибка типа данных при чтении Excel (TypeError)"""
    mock_isfile.return_value = True
    mock_read_excel.side_effect = TypeError("Неверный тип данных в ячейках")

    result = read_excel_file("bad_transactions.xlsx")

    # Проверяем, что функция перехватила ошибку и вернула обычный список
    assert isinstance(result, list)
    # Проверяем, что этот список пустой
    assert len(result) == 0


@patch("src.excel_csv_reader.os.path.isfile")
def test_read_excel_file_not_found(mock_file: Any) -> None:
    """Тест: файл не существует, должен вернуться пустой список"""
    mock_file.return_value = False
    result = read_excel_file("transaction.xlsx")

    # Проверяем, что вернулся именно список
    assert isinstance(result, list)
    # Проверяем, что список пустой
    assert len(result) == 0


@patch("src.excel_csv_reader.pd.read_excel")
@patch("src.excel_csv_reader.os.path.isfile")
def test_read_excel_file_success(mock_isfile: Any, mock_read_excel: Any) -> None:
    """Тест: успешное чтение корректного Excel-файла"""
    mock_isfile.return_value = True

    # Создаем фейковый DataFrame, который вернет pd.read_excel внутри функции
    fake_df = pd.DataFrame([{"id": 123, "amount": 100}])
    mock_read_excel.return_value = fake_df

    result = read_excel_file("transactions.xlsx")

    # Проверяем, что на выходе получили обычный список, а не DataFrame
    assert isinstance(result, list)
    # Сравниваем полученный результат напрямую со списком словарей
    assert result == [{"id": 123, "amount": 100}]


@patch("src.excel_csv_reader.pd.read_csv")
@patch("src.excel_csv_reader.os.walk")
@patch("src.excel_csv_reader.os.path.isfile")
def test_read_csv_file_smart_search_success(mock_isfile: Any, mock_walk: Any, mock_read_csv: Any) -> None:
    """Тест: файла нет по прямому пути, но "smart" поиск нашел его в подпапке"""
    mock_isfile.return_value = False  # Прямой путь не найден

    # Имитируем, что os.walk нашел наш файл 'transactions.csv' в папке 'data'
    mock_walk.return_value = [("/project/data", [], ["transactions.csv"])]

    fake_df = pd.DataFrame([{"id": 999}])
    mock_read_csv.return_value = fake_df

    result = read_csv_file("transactions.csv")

    # Проверяем, что вернулся именно список, и сравниваем его напрямую
    assert isinstance(result, list)
    assert result == [{"id": 999}]
