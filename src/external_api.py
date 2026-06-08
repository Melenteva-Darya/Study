import os
from typing import Any

import requests
from dotenv import load_dotenv

current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(current_dir)
dotenv_path = os.path.join(project_root, ".env")
load_dotenv(dotenv_path)


def currency_conversion(transaction: list[dict[str, Any]]) -> float | None:
    """Принимает транзакцию и возвращает сумму в рублях (float),
    при необходимости скачивая курсы ЦБ РФ из ссылки в .env"""
    transaction_dict = transaction[0]
    operation_amount = transaction_dict.get("operationAmount", {})

    the_amount = float(operation_amount.get("amount", 0.0))
    currency_code = operation_amount.get("currency", {}).get("code", "RUB")

    if currency_code == "RUB":
        return the_amount

    if currency_code in ["USD", "EUR"]:
        try:
            url = os.getenv("CBR_RATES_URL")
            response = requests.get(url, timeout=5)  # type: ignore

            data = response.json()
            rate = data["Valute"][currency_code]["Value"]

            result_rub = the_amount * rate
            return round(result_rub, 2)  # type: ignore

        except Exception as e:
            print(f"Ошибка при получении курсов валют: {e}")
            raise

    return the_amount
