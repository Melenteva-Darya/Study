from mypyc.primitives.misc_ops import yield_from_except_op


def filter_by_currency(transactions, currency=""):
    """Функция выводит список словарей, содержащие только те транзакции,
       где валюта операции соответствует заданной."""
    if currency == "":
        raise ValueError("Необходимо указать валюту для поиска.")

    result_currency = (dictionary for dictionary in transactions if
                       dictionary.get("operationAmount", {}).get("currency", {}).get("code") == currency)
    return result_currency


def transaction_descriptions(transactions):
    """Функция-генератор, которая принимает список словарей и
    поочередно возвращает описание каждой операции."""
    for operation in transactions:
        yield operation.get("description", "")


def card_number_generator(start, stop):
    """Генератор, который выдает номера банковских карт в формате XXXX XXXX XXXX XXXX
       в заданном диапазоне от start до stop включительно."""
    for number in range(start, stop + 1):
        str_number = f"{number:016d}"
        number_card = f"{str_number[:4]} {str_number[4:8]} {str_number[8:12]} {str_number[12:16]}"
        yield number_card

