from typing import Any


def filter_by_state(list_state: list[dict[str, Any]], state: str = "EXECUTED") -> Any:
    """Функция выводит список словарей, содержащие только те словари, у которых ключ
    state соответствует указанному значению."""

    if not list_state:
        return "Ошибка: список пуст!"

    if state == "":
        state = "EXECUTED"

    result_state = []
    for dictionary in list_state:
        if dictionary["state"] == state:
            result_state.append(dictionary)

    return result_state


def sort_by_date(list_data: list[dict[str, Any]], reverse=True) -> Any:
    """Функция сортирует список по дате"""

    if not list_data:
        return "Ошибка: список пуст!"

    if reverse == "":
        reverse = True

    result_data = sorted(list_data, key=lambda x: x["date"], reverse=reverse)
    return result_data


print(sort_by_date([{'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
       {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
       {'id': 594226727, 'state': 'CANCELED', 'date': '2018-06-30T21:27:25.241689'},
       {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}]))
