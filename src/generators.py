def filter_by_currency(transactions, currency=""):
    """Функция выводит список словарей, содержащие только те транзакции,
       где валюта операции соответствует заданной."""
    if currency == "":
        raise ValueError("Необходимо указать валюту для поиска.")

    result_currency = (dictionary for dictionary in transactions if
                       dictionary.get("operationAmount", {}).get("currency", {}).get("code") == currency)
    return result_currency
