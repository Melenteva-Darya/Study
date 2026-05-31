import os
import pytest
from src.decorators import log


def test_console_success(capsys):
    """Тест успешного выполнения функции с выводом в консоль"""

    @log()
    def add(a, b):
        return a + b

    result = add(3, 5)

    # Проверяем возвращаемое значение функции
    assert result == 8

    # Перехватываем print() с помощью capsys
    captured = capsys.readouterr()
    assert captured.out == "add ok\n"


def test_console_error(capsys):
    """Тест перехвата исключения с выводом в консоль"""

    @log()
    def divide(a, b):
        return a / b

    with pytest.raises(ZeroDivisionError):
        divide(10, 0)

    captured = capsys.readouterr()
    assert captured.out == "divide error: ZeroDivisionError. Inputs: (10, 0), {}\n"


def test_file_success(capsys):
    """Тест успешного выполнения функции с записью в файл"""
    filename = "test_success.log"

    @log(filename=filename)
    def greet(name):
        return f"Hello, {name}"

    try:
        greet("Alice")

        captured = capsys.readouterr()
        assert captured.out == ""

        with open(filename, "r", encoding="utf-8") as f:
            content = f.read()
        assert content == "greet ok\n"

    finally:
        if os.path.exists(filename):
            os.remove(filename)


def test_file_error(capsys):
    """Тест перехвата исключения с записью в файл"""
    filename = "test_error.log"

    @log(filename=filename)
    def get_element(lst, index):
        return lst[index]

    try:
        with pytest.raises(IndexError):
            get_element([10, 20], 5)

        captured = capsys.readouterr()
        assert captured.out == ""

        with open(filename, "r", encoding="utf-8") as f:
            content = f.read()
        assert content == "get_element error: IndexError. Inputs: ([10, 20], 5), {}\n"

    finally:
        if os.path.exists(filename):
            os.remove(filename)
