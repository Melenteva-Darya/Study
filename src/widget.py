from masks import get_mask_account, get_mask_card_number


def mask_account_card(payment_method: str) -> str:
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
        else:
            return f"Ошибка: строка {method} содержит недопустимые символы!"

    return " ".join(list_result)


def get_date(iso_format: str) -> str:
    list_iso_format = iso_format.split("T")
    for numbers in list_iso_format:
        year, month, day = numbers.split("-")

        return f"{day}.{month}.{year}"
