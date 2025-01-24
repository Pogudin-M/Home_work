from typing import Any, Dict, Iterator, List


def filter_by_currency(
    transactions: List[Dict[str, Any]], currency_code: str
) -> Iterator[Dict[str, Any]]:
    """
    Генератор, который фильтрует транзакции по валюте.

    :param transactions: Список словарей, представляющих транзакции.
    :param currency_code: Код валюты для фильтрации (например, "USD").
    :yield: Транзакции, соответствующие заданной валюте.
    """
    for transaction in transactions:
        if (
            "operationAmount" in transaction
            and "currency" in transaction["operationAmount"]
            and transaction["operationAmount"]["currency"].get("code") == currency_code
        ):
            yield transaction  # Если валюта совпадает, выдаем транзакцию


def transaction_descriptions(transactions: List[Dict[str, Any]]) -> Iterator[str]:
    """
    Генератор, который возвращает описание каждой транзакции по очереди.

    :param transactions: Список словарей, представляющих транзакции.
    :yield: Описание каждой транзакции. Если описание отсутствует, возвращает пустую строку.
    """
    # Проходим по каждой транзакции в списке
    for transaction in transactions:
        # Проверяем, есть ли описание в транзакции
        if "description" in transaction:
            yield transaction["description"]  # Если есть, возвращаем его
        else:
            yield ""  # Если нет, возвращаем пустую строку


def card_number_generator(start: int, end: int) -> Iterator[str]:
    """
    Генератор, который выдает номера банковских карт в формате XXXX XXXX XXXX XXXX.

    :param start: Начальное значение в диапазоне.
    :param end: Конечное значение в диапазоне.
    :yield: Номер карты в формате XXXX XXXX XXXX XXXX.
    """
    # Проходим по диапазону от start до end (включительно)
    for number in range(start, end + 1):
        # Форматируем номер с ведущими нулями и разделителями
        formatted_number = (
            f"{number:016d}"  # Форматируем число до 16 символов с ведущими нулями
        )
        # Возвращаем номер в формате XXXX XXXX XXXX XXXX
        yield f"{formatted_number[:4]} {formatted_number[4:8]} {formatted_number[8:12]} {formatted_number[12:16]}"
