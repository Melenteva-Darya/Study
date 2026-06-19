import re
from collections import Counter
from typing import Any


def process_bank_search(data: list[dict[str, Any]], search: str) -> list[dict[str, Any]]:
    """Универсальный поиск по всем полям. Приводит любые типы к строке."""
    dictionary_search = []

    for dict_ in data:
        for value in dict_.values():
            if re.search(search, str(value), flags=re.IGNORECASE):
                dictionary_search.append(dict_)
                break

    return dictionary_search


def process_bank_operations(data: list[dict[str, Any]], categories: list[str]) -> dict[str, int]:
    """Подсчитывает количество операций для каждой заданной категории из поля description."""
    all_descriptions = [dict_.get("description", "") for dict_ in data]

    # Подсчитываем частоту всех описаний в одну строчку
    counted_data = Counter(all_descriptions)

    # Собираем итоговый словарь. Если категории нет в файле — ставим 0
    result = {}
    for category in categories:
        result[category] = counted_data.get(category, 0)

    return result
