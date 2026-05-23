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


def sort_by_date(list_data: list[dict[str, Any]], reverse: bool | str = True) -> list[dict[str, Any]] | str:
    """Функция сортирует список по дате"""

    if not list_data:
        return "Ошибка: список пуст!"

    if reverse == "":
        reverse = True
    for x in list_data:
        if "date" not in x:
            return "Ошибка: неверный формат даты в списке!"

            # Проверяем, что дата — это строка и в ней есть два дефиса
        if not isinstance(x["date"], str) or x["date"].count("-") < 2:
            return "Ошибка: неверный формат даты в списке!"

    return sorted(list_data, key=lambda x: x["date"], reverse=bool(reverse))
