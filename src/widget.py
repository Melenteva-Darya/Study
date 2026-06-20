from src.masks import get_mask_account
from src.masks import get_mask_card_number


def mask_account_card(payment_method: str) -> str:
    """Маскирует номер карты или счета в строке с названием платежного метода."""
    list_payment_method = payment_method.split(" ")
    list_result = []
    for method in list_payment_method:
        if method.isdigit():
            if len(method) == 20:
                list_result.append(get_mask_account(method))
            elif len(method) == 16:
                mask_card_number = get_mask_card_number(method)
                list_result.append(mask_card_number)
            else:
                return "Ошибка: неверное количество цифр (нужно 16 или 20)!"
        elif method.isalpha():
            list_result.append(method)
        elif not payment_method:
            return "Ошибка: пустая строка!"
        else:
            return "Ошибка: строка содержит недопустимые символы!"

    return " ".join(list_result)


def get_date(iso_format: str) -> str:
    """Преобразует строку даты из формата YYYY-MM-DD в формат DD.MM.YYYY с валидацией."""
    iso_format = iso_format.strip()

    if not iso_format:
        return "Ошибка: пустая строка!"

    if "T" in iso_format:
        date_part = iso_format.split("T")[0]
        date_part = date_part.split(" ")[-1]
    else:
        date_part = iso_format.split(" ")[-1]

    if date_part.count("-") != 2:
        return "Ошибка: неверный формат даты!"

    parts = date_part.split("-")
    year = parts[0]
    month = parts[1]
    day = parts[2]

    if not (year.isdigit() and month.isdigit() and day.isdigit()) or len(year) != 4:
        return "Ошибка: неверный формат даты!"

    return f"{day}.{month}.{year}"
