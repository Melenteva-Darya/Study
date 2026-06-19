from typing import Any

from src.bank_processing import process_bank_search
from src.excel_csv_reader import read_csv_file
from src.excel_csv_reader import read_excel_file
from src.generators import filter_by_currency
from src.processing import filter_by_state
from src.processing import sort_by_date
from src.utils import get_financial_transactions
from src.widget import get_date
from src.widget import mask_account_card


def print_final_transactions(transactions_list: list) -> None:
    """Выводит ответ если нет ни одной транзакции."""
    if not transactions_list:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
        return

    print(f"Всего банковских операций в выборке: {len(transactions_list)}\n")

    for tx in transactions_list:
        # 1. Применяем вашу функцию даты
        date_raw = tx.get("date", "")
        date_formatted = get_date(date_raw)
        if "Ошибка" in date_formatted:
            date_formatted = "??.%m.%Y"  # заглушка, если дата сломана

        description = tx.get("description", "Без описания")

        # 2. Применяем вашу функцию маскирования карт и счетов
        from_info = tx.get("from", "")
        to_info = tx.get("to", "")

        # Безопасно маскируем через вашу функцию, если поле заполнено
        from_formatted = mask_account_card(from_info) if from_info else ""
        to_formatted = mask_account_card(to_info) if to_info else ""

        # Если ваши функции вернули текст ошибки, выводим исходную строку
        if "Ошибка" in from_formatted:
            from_formatted = from_info
        if "Ошибка" in to_formatted:
            to_formatted = to_info

        # Собираем стрелочку направления "откуда -> куда"
        if from_formatted and to_formatted:
            direction = f"{from_formatted} -> {to_formatted}"
        elif to_formatted:
            direction = to_formatted
        else:
            direction = from_formatted

        # 3. Извлекаем сумму и валюту операции
        amount = tx.get("operationAmount", {}).get("amount", "0")
        currency = tx.get("operationAmount", {}).get("currency", {}).get("name", "руб.")
        # Если в файле написано RUB, заменяем на "руб." для красивого вывода
        if currency == "RUB":
            currency = "руб."

        # Выводим финальный блок транзакции в консоль
        print(f"{date_formatted} {description}")
        if direction:
            print(direction)
        print(f"Сумма: {amount} {currency}\n")


def get_user_file_choice() -> list[dict[str, Any]]:
    """Запрашивает у пользователя тип файла и возвращает транзакции."""
    while True:
        choice_item = input("Введите необходимый пункт меню: ").strip()
        if choice_item == "1":
            print("Для обработки выбран JSON-файл.")
            return get_financial_transactions("operations.json")
        elif choice_item == "2":
            print("Для обработки выбран CSV-файл.")
            return read_csv_file("transactions.csv")
        elif choice_item == "3":
            print("Для обработки выбран XLSX-файл.")
            return read_excel_file("transactions_excel.xlsx")
        else:
            print("Ошибка: пожалуйста, выберете пункт: 1, 2 или 3")


def get_user_status_filter(transactions: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """Запрашивает статус и фильтрует транзакции."""
    print(
        "Введите статус, по которому необходимо выполнить фильтрацию.\n"
        "Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING"
    )
    while True:
        choice_status = input("Введите статус: ").strip().upper()
        if choice_status in ["EXECUTED", "CANCELED", "PENDING"]:
            print(f"Операции отфильтрованы по статусу '{choice_status}'")
            return filter_by_state(transactions, choice_status)
        else:
            print(
                f"Статус операции {choice_status} недоступен.\n"
                f"Введите статус, по которому необходимо выполнить фильтрацию.\n"
                f"Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING"
            )


def handle_date_sorting(transactions: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """Обрабатывает сортировку по дате."""
    while True:
        print("Отсортировать операции по дате? Да/Нет")
        choice_status = input("Введите ответ: ").strip().lower()
        if choice_status == "да":
            while True:
                print("Отсортировать по возрастанию или по убыванию?")
                choice_sort_date = input("Введите ответ: ").strip().lower()
                if "возраст" in choice_sort_date:
                    return sort_by_date(transactions, reverse=False)
                elif "убыва" in choice_sort_date:
                    return sort_by_date(transactions, reverse=True)
                else:
                    print("Выберете по возрастанию или по убыванию?")
        elif choice_status == "нет":
            return transactions
        else:
            print("Ошибка: пожалуйста, ответьте 'Да' или 'Нет'.")


def handle_currency_filtering(transactions: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """Обрабатывает фильтрацию по валюте."""
    while True:
        print("Выводить только рублевые транзакции? Да/Нет")
        choice_sort_rub = input("Введите ответ: ").strip().lower()
        if choice_sort_rub == "да":
            return list(filter_by_currency(transactions, currency="RUB"))
        elif choice_sort_rub == "нет":
            return transactions
        else:
            print("Ошибка: пожалуйста, выберете 'Да' или 'Нет'.")


def handle_word_filtering(transactions: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """Обрабатывает фильтрацию по ключевому слову."""
    while True:
        print("Отфильтровать список транзакций по определенному слову в описании? Да/Нет")
        choice_sort_word = input("Введите ответ: ").strip().lower()
        if choice_sort_word == "да":
            print("Введите слово, по которому необходимо отфильтровать транзакции:")
            choice_sort_word_ = input("Введите ответ: ").strip().lower()
            return process_bank_search(transactions, choice_sort_word_)
        elif choice_sort_word == "нет":
            return transactions
        else:
            print("Ошибка: пожалуйста, ответьте 'Да' или 'Нет'.")


def main() -> None:
    """Основная логика программы."""
    print(
        "Привет! Добро пожаловать в программу работы \n"
        "    с банковскими транзакциями. \n"
        "    Выберите необходимый пункт меню:\n"
        "    1. Получить информацию о транзакциях из JSON-файла\n"
        "    2. Получить информацию о транзакциях из CSV-файла\n"
        "    3. Получить информацию о транзакциях из XLSX-файла"
    )

    transactions = get_user_file_choice()
    transactions = get_user_status_filter(transactions)
    transactions = handle_date_sorting(transactions)
    transactions = handle_currency_filtering(transactions)
    transactions = handle_word_filtering(transactions)

    print("Распечатываю итоговый список транзакций...")
    print_final_transactions(transactions)
