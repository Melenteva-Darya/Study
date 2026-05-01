from black.linegen import replace

from masks import get_mask_card_number, get_mask_account

def mask_account_card(payment_method):
    list_payment_method = payment_method.split(" ")
    list_result = []
    for method in list_payment_method:
        if method.isdigit() and len(method) == 16:
            mask_card_number = get_mask_card_number(method)
            list_result.append(mask_card_number)
        elif method.isdigit() and len(method) == 20:
            mask_account = get_mask_account(method)
            list_result.append(mask_account)
        elif method.isalpha():
            list_result.append(method)
    print(list_result)

mask_account_card("Maestro 7000792289606361")