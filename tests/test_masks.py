from typing import Optional

import pytest

from src.masks import get_mask_account, get_mask_card_number


# Тесты для функции get_mask_card_number
@pytest.mark.parametrize(
    "value, expected",
    [
        ("1234567812345678", "1234 56** **** 5678"),
        ("1234 5678 1234 5678", "1234 56** **** 5678"),
        ("123456781234", "**** **** ****"),
        ("", ""),
        (None, ""),
    ],
)
def test_get_mask_card_number(value: Optional[str], expected: Optional[str]) -> None:
    assert get_mask_card_number(value) == expected


# Тесты для функции get_mask_account
def test_get_mask_account(account: str) -> None:
    assert get_mask_account(account) == "****************7890"
