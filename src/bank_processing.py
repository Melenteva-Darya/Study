import re
from typing import Any


def process_bank_search(data:list[dict], search:str)-> list[list[Any]]:
    dictionary_search = []
    for dict_ in data:
        if search:
            found_value = re.search(search, dict_, flags=re.IGNORECASE)
            dictionary_search.append(found_value)

    return dictionary_search


def process_bank_operations(data:list[dict], categories:list)->dict:
    pass
