import functools
import logging
from typing import Any, Callable, Optional


def log(filename: Optional[str] = None) -> Callable:
    """
    Декоратор для логирования выполнения функции.

    :param filename: Имя файла для записи логов. Если не указано, логи выводятся в консоль.
    """

    def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
        logger = logging.getLogger(f"FunctionLogger_{func.__name__}")
        logger.setLevel(logging.INFO)

        # Объявляем handler здесь, чтобы он был виден за пределами if/else
        handler: logging.Handler
        if filename:
            handler = logging.FileHandler(filename, mode="a", encoding="utf-8")
        else:
            handler = logging.StreamHandler()

        logger.addHandler(handler)

        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            try:
                logger.info(
                    f"Начало выполнения {func.__name__} с аргументами: {args}, {kwargs}"
                )
                result = func(*args, **kwargs)
                logger.info(f"{func.__name__} успешно выполнена")
                return result
            except Exception as e:
                logger.error(
                    f"{func.__name__} ошибка: {type(e).__name__}. Входные данные: {args}, {kwargs}"
                )
                raise e
            finally:
                for h in list(logger.handlers):
                    h.close()
                    logger.removeHandler(h)

        return wrapper

    return decorator
