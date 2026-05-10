def filter_by_state(list_state: list[dict], state: str = "EXECUTED") -> list[dict]:
    """Функция выводит список словарей, содержащие только те словари, у которых ключ
state соответствует указанному значению."""
    result_state = []
    for dictionary in list_state:
        if dictionary["state"] == state:
            result_state.append(dictionary)
    return result_state


def sort_by_date(list_data: list[dict], reverse=True) -> list[dict]:
    """Функция сортирует список по дате"""
    result_data = sorted(list_data, key=lambda x: x["date"], reverse=reverse)
    return result_data
