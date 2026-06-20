from typing import Any

from src.main import main
from src.main import print_final_transactions


def test_main_scenario_success(monkeypatch: Any, capsys: Any, mock_transactions: list[dict[str, Any]]) -> None:
    """Тест проверяет успешное прохождение пользователя по всему меню с фильтрацией по слову."""
    monkeypatch.setattr("src.main.get_financial_transactions", lambda path: mock_transactions)

    inputs = [
        "1",  # Выбор пункта меню (1 - JSON)
        "EXECUTED",  # Ввод статуса
        "да",  # Отсортировать по дате? Да
        "по убыванию",  # Направление сортировки
        "да",  # Только рублевые транзакции? Да
        "да",  # Отфильтровать по слову? Да
        "вклада",  # Слово для фильтрации
    ]

    input_generator = (i for i in inputs)
    monkeypatch.setattr("builtins.input", lambda _: next(input_generator))

    main()

    captured = capsys.readouterr()
    output = captured.out

    assert "Для обработки выбран JSON-файл." in output
    assert "Операции отфильтрованы по статусу 'EXECUTED'" in output
    assert "Распечатываю итоговый список транзакций..." in output
    assert "Открытие вклада" in output


def test_main_invalid_status_retry(monkeypatch: Any, capsys: Any, mock_transactions: list[dict[str, Any]]) -> None:
    """Тест проверяет реакцию интерфейса на неверный статус и последующий ввод корректных данных."""
    monkeypatch.setattr("src.main.get_financial_transactions", lambda path: mock_transactions)

    inputs = [
        "1",  # Выбор пункта меню (1 - JSON)
        "test_error",  # Неверный статус (программа должна повторить запрос)
        "EXECUTED",  # Правильный статус
        "нет",  # Отсортировать по дате? Нет
        "нет",  # Только рублевые транзакции? Нет
        "нет",  # Фильтр по слову в описании? Нет
    ]

    input_generator = (i for i in inputs)
    monkeypatch.setattr("builtins.input", lambda _: next(input_generator))

    main()

    captured = capsys.readouterr()
    output = captured.out

    assert "Статус операции TEST_ERROR недоступен." in output


def test_print_empty_transactions(capsys: Any) -> None:
    """Тест проверяет корректность текстового вывода при пустом списке отфильтрованных транзакций."""
    print_final_transactions([])

    captured = capsys.readouterr()
    assert "Не найдено ни одной транзакции, подходящей под ваши условия фильтрации" in captured.out
