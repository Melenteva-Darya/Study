from src.processing import sort_by_date


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
        break
    elif choice_item == "2":
        print("Для обработки выбран CSV-файл.")
        break
    elif choice_item == "3":
        print("Для обработки выбран XLSX-файл.")
        break
    else:
        print("Выбран несуществующий пункт. Выберете пункт: 1, 2 или 3")

print("""Введите статус, по которому необходимо выполнить фильтрацию. 
Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING""")

while True:
    choice_status = input("Введите статус: ").upper()

    if choice_status == "EXECUTED":
        print(f"Операции отфильтрованы по статусу {choice_status}")
        break
    elif choice_status == "CANCELED":
        print(f"Операции отфильтрованы по статусу {choice_status}")
        break
    elif choice_status == "PENDING":
        print(f"Операции отфильтрованы по статусу {choice_status}")
        break
    else:
        print(f"""Статус операции {choice_status} недоступен.
Введите статус, по которому необходимо выполнить фильтрацию. 
Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING""")


print("Отсортировать операции по дате? Да/Нет")
choice_status = input("Введите ответ: ").strip().lower()

if choice_status == "да":
    # Уточняем направление ТОЛЬКО если пользователь ответил "да"
    print("Отсортировать по возрастанию или по убыванию?")
    choice_sort_date = input("Пользователь: ").strip().lower()

    # 3. Вот ОНА — ваша функция сортировки, которая применяется на основе выбора
    if "возраст" in choice_sort_date:
        transactions = sort_by_date(transactions, reverse=False)
    else:
        transactions = sort_by_date(transactions, reverse=True)

print("Отсортировать по возрастанию или по убыванию?")
choice_sort_date = input("Введите ответ: ").lower()

print("Выводить только рублевые транзакции? Да/Нет")
choice_sort_rub = input("Введите ответ: ").lower()

print("Отфильтровать список транзакций по определенному слову в описании? Да/Нет")
choice_sort_list = input("Введите ответ: ").lower()

print("Распечатываю итоговый список транзакций...")

