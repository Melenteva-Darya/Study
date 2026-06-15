import logging
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
log_dir = os.path.abspath(os.path.join(script_dir, "..", "logs"))
log_file_path = os.path.join(log_dir, "masks.log")

utils_logger = logging.getLogger(__name__)
utils_logger.setLevel(logging.DEBUG)
file_handler = logging.FileHandler(log_file_path, mode="w", encoding="utf-8")

file_formatter = logging.Formatter("%(asctime)s %(filename)s %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)

utils_logger.addHandler(file_handler)
utils_logger.debug("Debug message")


def get_mask_card_number(card_number: str) -> str:
    """Функция маскирует номер карты"""
    list_numbers = []
    utils_logger.info("Программа успешно запущена")

    if len(card_number) == 16:
        for i in range(0, len(card_number), 4):
            numbers = card_number[i: i + 4]
            list_numbers.append(numbers)
        if len(list_numbers) >= 4:
            list_numbers[1] = list_numbers[1][:2] + "**"
            list_numbers[2] = "****"

    elif not card_number:
        utils_logger.warning("Ошибка: пустая строка")
        return "Ошибка: пустая строка!"

    else:
        utils_logger.warning("Ошибка: неверное количество цифр")
        return "Ошибка: неверное количество цифр (нужно 16)!"

    utils_logger.info("Программа успешно завершена")
    return " ".join(list_numbers)


def get_mask_account(score: str) -> str:
    """Функция маскирует номер счета"""
    result_score = ""
    list_score = []

    utils_logger.info("Программа успешно запущена")
    if len(score) == 20:
        for i in range(0, len(score), 4):
            numbers = score[i: i + 4]
            list_score.append(numbers)
        if len(list_score) >= 4:
            result_score = "**" + list_score[-1]
        utils_logger.info("Программа успешно завершена")
        return "".join(result_score)
    elif not score:
        utils_logger.warning("Ошибка: пустая строка")
        return "Ошибка: пустая строка!"
    else:
        utils_logger.error("Ошибка: неверное количество цифр (нужно 20)!")
        return "Ошибка: неверное количество цифр (нужно 20)!"
