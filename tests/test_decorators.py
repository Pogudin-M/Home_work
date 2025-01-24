import os
import sys

import pytest

from src.decorators import log

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


@log(filename="test_log.txt")
def successful_function(x: int, y: int) -> int:
    return x + y


@log(filename="test_log.txt")
def error_function(x: int, y: int) -> float:
    return x / y  # Деление на ноль вызовет ошибку


def test_successful_function(capsys: pytest.CaptureFixture) -> None:
    result = successful_function(1, 2)
    assert result == 3

    # Проверка логов с кодировкой 'utf-8'
    with open("test_log.txt", "r", encoding="utf-8") as f:
        logs = f.read()
    assert "успешно выполнена" in logs


def test_error_function(capsys: pytest.CaptureFixture) -> None:
    with pytest.raises(ZeroDivisionError):
        error_function(1, 0)

    # Проверка логов с кодировкой 'utf-8'
    with open("test_log.txt", "r", encoding="utf-8") as f:
        logs = f.read()
    assert "ошибка: ZeroDivisionError" in logs
