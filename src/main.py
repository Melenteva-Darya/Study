from src.bank_processing import process_bank_search
from src.excel_csv_reader import read_csv_file
from src.excel_csv_reader import read_excel_file
from src.generators import filter_by_currency
from src.processing import sort_by_date
from src.processing import filter_by_state
from src.utils import get_financial_transactions

print("""Привет! Добро пожаловать в программу работы 
с банковскими транзакциями. 
Выберите необходимый пункт меню:
1. Получить информацию о транзакциях из JSON-файла
2. Получить информацию о транзакциях из CSV-файла
3. Получить информацию о транзакциях из XLSX-файла""")

while True:
    choice_item = input("Введите необходимый пункт меню: ")

    if choice_item == "1":
        print("Для обработки выбран JSON-файл.")
        transactions = get_financial_transactions("operations.json")
        break
    elif choice_item == "2":
        print("Для обработки выбран CSV-файл.")
        transactions = read_csv_file("transactions.csv")
        break
    elif choice_item == "3":
        print("Для обработки выбран XLSX-файл.")
        transactions = read_excel_file("transactions_excel.xlsx")
        break
    else:
        print("Ошибка: пожалуйста, выберете пункт: 1, 2 или 3")


print("""Введите статус, по которому необходимо выполнить фильтрацию. 
Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING""")

while True:
    choice_status = input("Введите статус: ").upper()

    if choice_status == "EXECUTED":
        print(f"Операции отфильтрованы по статусу {choice_status}")
        transactions = filter_by_state(transactions, "EXECUTED")
        break
    elif choice_status == "CANCELED":
        print(f"Операции отфильтрованы по статусу {choice_status}")
        transactions = filter_by_state(transactions, "CANCELED")
        break
    elif choice_status == "PENDING":
        print(f"Операции отфильтрованы по статусу {choice_status}")
        transactions = filter_by_state(transactions, "PENDING")
        break
    else:
        print(f"""Статус операции {choice_status} недоступен.
Введите статус, по которому необходимо выполнить фильтрацию. 
Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING""")

while True:
    print("Отсортировать операции по дате? Да/Нет")
    choice_status = input("Введите ответ: ").strip().lower()

    if choice_status == "да":
        while True:

            # Уточняем направление ТОЛЬКО если пользователь ответил "да"
            print("Отсортировать по возрастанию или по убыванию?")
            choice_sort_date = input("Введите ответ: ").strip().lower()

            # функция сортировки, которая применяется на основе выбора
            if "возраст" in choice_sort_date:
                transactions = sort_by_date(transactions, reverse=False)
                break

            elif "убыва" in choice_sort_date:
                transactions = sort_by_date(transactions, reverse=True)
                break

            else:
                print("Выберете по возрастанию или по убыванию?")
        break
    elif choice_status == "нет":
        break
    else:
        print("Ошибка: пожалуйста, ответьте 'Да' или 'Нет'.")

print("Выводить только рублевые транзакции? Да/Нет")
choice_sort_rub = input("Введите ответ: ").lower()
if choice_status == "да":
    transactions = filter_by_currency(transactions, "RUB")

print("Отфильтровать список транзакций по определенному слову в описании? Да/Нет")
choice_sort_list = input("Введите ответ: ").lower()
if choice_status == "да":
    transactions = process_bank_search(transactions, choice_sort_list)

print("Распечатываю итоговый список транзакций...")
print(transactions)
