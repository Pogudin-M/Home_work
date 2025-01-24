from typing import Any, Dict, List

import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


# Тест, проверяющий фильтрацию по валюте
def test_filter_by_currency(transaction: List[Dict[str, Any]]) -> None:
    usd_transactions = list(filter_by_currency(transaction, "USD"))
    gbp_transactions = list(filter_by_currency(transaction, "GBP"))

    assert len(usd_transactions) == 3  # Должно быть 3 транзакции в USD
    # Проверяем, что эти транзакции имеют правильные суммы
    assert len(gbp_transactions) == 0  # Не должно быть транзакций в GBP
    assert usd_transactions[0]["operationAmount"]["amount"] == "9824.07"
    assert usd_transactions[1]["operationAmount"]["amount"] == "79114.93"
    assert usd_transactions[2]["operationAmount"]["amount"] == "56883.54"


# Тест, проверяющий работу функции с пустым списком
def test_filter_by_currency_empty_list() -> None:
    assert (
        list(filter_by_currency([], "USD")) == []
    )  # Пустой список должен возвращать пустой список


@pytest.mark.parametrize(
    "transaction, expected_descriptions",
    [
        (
            [
                {"id": 1, "description": "Перевод организации"},
                {"id": 2, "description": "Перевод со счета на счет"},
                {"id": 3, "description": "Перевод с карты на карту"},
            ],
            [
                "Перевод организации",
                "Перевод со счета на счет",
                "Перевод с карты на карту",
            ],
        ),
        (
            [
                {"id": 1, "description": "Перевод организации"},
                {"id": 2},  # Эта транзакция без описания
            ],
            ["Перевод организации", ""],  # Пустая строка для транзакции без описания
        ),
        ([], []),  # Пустой список транзакций  # Ожидаем пустой список описаний
    ],
)
def test_transaction_descriptions(
    transaction: Any, expected_descriptions: list
) -> None:
    descriptions = list(transaction_descriptions(transaction))
    assert (
        descriptions == expected_descriptions
    )  # Проверяем, что описания соответствуют ожидаемым


# Тест генератора номеров карт
def test_card_number_generator() -> None:
    # Генерируем номера карт от 1 до 5
    card_numbers = list(card_number_generator(1, 5))
    expected_numbers = [
        "0000 0000 0000 0001",
        "0000 0000 0000 0002",
        "0000 0000 0000 0003",
        "0000 0000 0000 0004",
        "0000 0000 0000 0005",
    ]
    assert (
        card_numbers == expected_numbers
    )  # Проверяем, что номера совпадают с ожидаемыми значениями


# Тест крайних значений
def test_card_number_generator_extreme() -> None:
    first_card = next(card_number_generator(1, 1))
    assert first_card == "0000 0000 0000 0001"  # Проверяем первый номер
    last_card = next(card_number_generator(9999999999999999, 9999999999999999))
    assert last_card == "9999 9999 9999 9999"  # Проверяем последний номер
