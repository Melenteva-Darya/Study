import re
from collections import Counter


def process_bank_search(data:list[dict], search:str)-> list[dict]:
    """Универсальный поиск по всем полям. Приводит любые типы к строке."""
    dictionary_search = []

    for dict_ in data:
        for value in dict_.values():
            if re.search(search, str(value), flags=re.IGNORECASE):
                dictionary_search.append(dict_)
                break

    return dictionary_search


def process_bank_operations(data:list[dict], categories:list)-> dict:
    """Подсчитывает количество операций для каждой заданной категории из поля description."""
    all_descriptions = [dict_.get("description", "") for dict_ in data]

    #  подсчитываем частота всех описаний в одну строчку
    counted_data = Counter(all_descriptions)

    # Собираем итоговый словарь. Если категории нет в файле — ставим 0
    result = {}
    for category in categories:
        result[category] = counted_data.get(category, 0)

    return result
