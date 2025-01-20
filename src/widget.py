from datetime import datetime
from typing import Optional

from src.masks import get_mask_account, get_mask_card_number  # Импорт функции маскировки


def mask_account_card(info: Optional[str]) -> Optional[str]:
    """
    Маскирует номер карты или счета.
    :param info: строка, содержащая тип и номер карты или счета.
    :return: строка с замаскированным номером.

    """
    card_types = ["Visa", "MasterCard", "Maestro"]

    if info is None:
        return None  # Возвращаем None, если входное значение None

    parts = info.split(" ")

    if mask_account_card is None:
        return ""  # Возвращаем пустую строку для None

    if len(parts) < 2:
        return ""

    card_type = " ".join(parts[:-1])  # Все части кроме последней
    number = parts[-1].replace(" ", "")  # Последняя часть - номер, убираем пробелы

    if card_type in card_types:
        masked_number = get_mask_card_number(
            number
        )  # Используйте функцию маскировки карты
    elif card_type == "Счет":
        masked_number = get_mask_account(number)  # Используйте функцию маскировки счета
    else:
        return ""

    return f"{card_type} {masked_number}"


def get_date(date_str: Optional[str]) -> Optional[str]:
    """
    Преобразует дату из строки ISO в формат ДД.ММ.ГГГГ.
    :param date_str: строка с датой в формате "YYYY-MM-DD:MM:SS".
    :return: строка с датой в формате "ДД.ММ.ГГГГ".

    """
    if get_date is None:
        return ""  # Возвращаем пустую строку для None
    if not date_str:
        return ""
    try:
        date_obj = datetime.fromisoformat(date_str)
        return date_obj.strftime("%d.%m.%Y")
    except ValueError:
        raise ValueError("Неверный формат даты")
