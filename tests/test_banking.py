from typing import Any

from src.bank_processing import process_bank_operations
from src.bank_processing import process_bank_search


def test_process_bank_search_success(sample_transactions: list[dict[str, Any]]) -> None:
    """Тест успешного поиска операций по описанию (регистронезависимый)."""
    result = process_bank_search(sample_transactions, "перевод")
    assert len(result) == 5
    # Проверяем, что в отфильтрованном списке есть транзакция с нужным ID
    assert any(t["id"] == 939719570 for t in result)


def test_process_bank_search_by_numeric_id(sample_transactions: list[dict[str, Any]]) -> None:
    """Тест поиска операции по её цифровому ID в строковом формате."""
    result = process_bank_search(sample_transactions, "895315941")
    assert len(result) == 1
    assert result[0]["id"] == 895315941


def test_process_bank_search_no_matches(sample_transactions: list[dict[str, Any]]) -> None:
    """Тест поиска слова, которого нет ни в одном описании или ID транзакции."""
    result = process_bank_search(sample_transactions, "абракадабра")
    assert len(result) == 0


def test_process_bank_search_with_missing_description(sample_transactions_2: list[dict[str, Any]]) -> None:
    """Тест корректной обработки транзакций, у которых описание отсутствует (равно None)."""
    result = process_bank_search(sample_transactions_2, "вклада")
    assert len(result) == 1
    assert result[0]["id"] == 222


def test_count_operations_by_category_success(sample_transactions: list[dict[str, Any]]) -> None:
    """Тест успешного подсчета операций по переданному списку категорий."""
    categories = ["Перевод организации", "Перевод со счета на счет", "Несуществующая"]
    result = process_bank_operations(sample_transactions, categories)

    assert result["Перевод организации"] == 2
    assert result["Перевод со счета на счет"] == 2
    assert result["Несуществующая"] == 0


def test_count_operations_by_category_with_zeros(sample_transactions: list[dict[str, Any]]) -> None:
    """Тест подсчета, когда ни одна операция в списке не совпадает с искомыми категориями."""
    categories = ["Оплата ЖКХ", "Покупка продуктов"]
    result = process_bank_operations(sample_transactions, categories)

    assert result["Оплата ЖКХ"] == 0
    assert result["Покупка продуктов"] == 0
