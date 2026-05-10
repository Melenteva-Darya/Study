from typing import Any


def filter_by_state(list_state: list[dict[str, Any]], state: str = "EXECUTED") -> list[dict[str, Any]]:
    """Функция выводит список словарей, содержащие только те словари, у которых ключ
    state соответствует указанному значению."""
    result_state = []
    for dictionary in list_state:
        if dictionary["state"] == state:
            result_state.append(dictionary)
    return result_state


def sort_by_date(list_data: list[dict[str, Any]], reverse=True) -> list[dict[str, Any]]:
    """Функция сортирует список по дате"""
    result_data = sorted(list_data, key=lambda x: x["date"], reverse=reverse)
    return result_data
