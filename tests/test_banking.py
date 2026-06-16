from src.bank_processing import process_bank_search
from src.bank_processing import process_bank_operations


def test_process_bank_search_success(sample_transactions_2):
    """Тест успешного поиска по слову без учета регистра."""
    # "перевод" маленькими буквами, хотя в словаре "Перевод" с большой
    result = process_bank_search(sample_transactions_2, "перевод")

    # Должно найтись 2 операции с описанием "Перевод организации"
    assert len(result) == 2
    assert result[0]["id"] == 111
    assert result[1]["id"] == 333


def test_process_bank_search_by_numeric_id(sample_transactions_2):
    """Тест поиска по числу (ID из JSON), приведенному к строке."""
    # Ищем строку "222", которая в словаре лежит как число 222
    result = process_bank_search(sample_transactions_2, "222")

    assert len(result) == 1
    assert result[0]["description"] == "Открытие вклада"


def test_process_bank_search_no_matches(sample_transactions_2):
    """Тест ситуации, когда совпадений вообще не найдено."""
    result = process_bank_search(sample_transactions_2, "Покупка акций")
    assert result == []


def test_process_bank_search_empty_data():
    """Тест работы функции с абсолютно пустым списком."""
    result = process_bank_search([], "Перевод")
    assert result == []


def test_count_operations_by_category_success(sample_transactions_2):
    """Тест правильного подсчета существующих категорий."""
    categories = ["Перевод организации", "Открытие вклада"]
    result = process_bank_operations(sample_transactions_2, categories)

    # Проверяем точные цифры подсчета
    assert result["Перевод организации"] == 2
    assert result["Открытие вклада"] == 1


def test_count_operations_by_category_with_zeros(sample_transactions_2):
    """Тест категории, которой нет в данных (должен вернуться 0)."""
    categories = ["Перевод организации", "Покупка акций"]
    result = process_bank_operations(sample_transactions_2, categories)

    assert result["Перевод организации"] == 2


def test_count_operations_by_category_empty_lists():
    """Тест, когда переданы пустые списки данных и категорий."""
    assert process_bank_operations([], []) == {}
    assert process_bank_operations([], ["Вклад"]) == {"Вклад": 0}
