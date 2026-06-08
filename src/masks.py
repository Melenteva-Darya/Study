import os
import logging

script_dir = os.path.dirname(os.path.abspath(__file__))
log_dir = os.path.abspath(os.path.join(script_dir, "..", "logs"))
log_file_path = os.path.join(log_dir, "masks.log")

utils_logger = logging.getLogger(__name__)
utils_logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler("logs/masks.log")

file_formatter = logging.Formatter('%(asctime)s %(filename)s %(levelname)s: %(message)s')
file_handler.setFormatter(file_formatter)

utils_logger.addHandler(file_handler)
utils_logger.debug('Debug message')


def get_mask_card_number(card_number: str) -> str:
    """Функция маскирует номер карты"""
    list_numbers = []
    if len(card_number) == 16:
        for i in range(0, len(card_number), 4):
            numbers = card_number[i : i + 4]
            list_numbers.append(numbers)
        if len(list_numbers) >= 4:
            list_numbers[1] = list_numbers[1][:2] + "**"
            list_numbers[2] = "****"
    elif not card_number:
        return "Ошибка: пустая строка!"
    else:
        return "Ошибка: неверное количество цифр (нужно 16)!"
    return " ".join(list_numbers)


def get_mask_account(score: str) -> str:
    """Функция маскирует номер счета"""
    result_score = ""
    list_score = []
    if len(score) == 20:
        for i in range(0, len(score), 4):
            numbers = score[i : i + 4]
            list_score.append(numbers)
        if len(list_score) >= 4:
            result_score = "**" + list_score[-1]
        return "".join(result_score)
    elif not score:
        return "Ошибка: пустая строка!"
    else:
        return "Ошибка: неверное количество цифр (нужно 20)!"
