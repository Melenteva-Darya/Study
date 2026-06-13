from unittest.mock import patch, mock_open

import pandas as pd
from pandas import DataFrame
from src.excel_csv_reader import read_csv_file, read_excel_file


@patch("src.excel_csv_reader.os.path.isfile")
def test_read_csv_file_not_found(mock_file: str) -> DataFrame:
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

@patch("src.excel_csv_reader.os.path.isfile")
def test_read_excel_file_not_found(mock_file: str) -> DataFrame:
    """Тест: файл не существует"""
    mock_file.return_value = False
    result = read_excel_file("transaction.csv")

    assert isinstance(result, pd.DataFrame)
    assert result.empty


@patch("src.excel_csv_reader.pd.read_excel")
@patch("src.excel_csv_reader.os.path.isfile")
def test_read_excel_file_success(mock_isfile: Any, mock_read_excel: Any) -> None:
    """Тест: успешное чтение корректного CSV-файла с одним аргументом"""
    mock_isfile.return_value = True
    fake_df = pd.DataFrame([{"id": 123, "amount": 100}])
    mock_read_excel.return_value = fake_df
    result = read_excel_file("transactions.csv")

    assert isinstance(result, pd.DataFrame)
    assert result.to_dict(orient="records") == [{"id": 123, "amount": 100}]