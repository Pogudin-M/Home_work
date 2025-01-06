from datetime import datetime

from src.masks import get_mask_account, get_mask_card_number  # Импорт функции маскировки


def mask_account_card(info: str) -> str:
    """
    Маскирует номер карты или счета.
    :param info: строка, содержащая тип и номер карты или счета.
    :return: строка с замаскированным номером.

    """
    card_types = ["Visa", "MasterCard", "Maestro"]
    parts = info.split(" ")

    if len(parts) < 2:
        raise ValueError("Неверный формат строки")

    card_type = " ".join(parts[:-1])  # Все части кроме последней
    number = parts[-1]  # Последняя часть - номер

    if card_type in card_types:
        masked_number = get_mask_card_number(
            number
        )  # Используйте функцию маскировки карты
    elif card_type == "Счет":
        masked_number = get_mask_account(number)  # Используйте функцию маскировки счета
    else:
        raise ValueError("Неизвестный тип карты или счета")

    return f"{card_type} {masked_number}"


def get_date(date_str: str) -> str:
    """
    Преобразует дату из строки ISO в формат ДД.ММ.ГГГГ.
    :param date_str: строка с датой в формате "YYYY-MM-DD:MM:SS".
    :return: строка с датой в формате "ДД.ММ.ГГГГ".

    """
    try:
        date_obj = datetime.fromisoformat(date_str)
        return date_obj.strftime("%d.%m.%Y")
    except ValueError:
        raise ValueError("Неверный формат даты")
