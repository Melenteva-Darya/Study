import functools
from typing import Any, Callable, Optional


def log(filename: Optional[str] = None) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
    """Декоратор log автоматически логирует начало и конец выполнения функции,
    а также ее результаты или возникшие ошибки.
    Параметры: filename (str, optional):
    Путь к файлу для записи логов. Если не задан, логи выводятся в консоль."""

    def my_decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            func_name = func.__name__

            try:
                result = func(*args, **kwargs)
                if filename:
                    with open(filename, "a", encoding="utf-8") as file_object:
                        file_object.write(f"{func_name} ok\n")
                else:
                    print(f"{func_name} ok")

                return result

            except Exception as error:
                error_name = type(error).__name__

                if filename:
                    with open(filename, "a", encoding="utf-8") as file_object:
                        file_object.write(f"{func_name} error: {error_name}. Inputs: {args}, {kwargs}\n")
                else:
                    print(f"{func_name} error: {error_name}. Inputs: {args}, {kwargs}")

                raise error

        return wrapper

    return my_decorator
