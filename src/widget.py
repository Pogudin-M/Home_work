from masks import get_mask_card_number, get_mask_account  # Импорт функции маскировки


def mask_account_card(info: str) -> str:
    """
    Маскирует номер карты или счета. :param info: строка, содержащая тип и номер карты или счета. :return: строка с замаскированным номером.

    """
    card_types = ['Visa', 'MasterCard', 'Maestro']
    parts = info.split(' ')

    if len(parts) < 2:
        raise ValueError("Неверный формат строки")

    card_type = ' '.join(parts[:-1])  # Все части кроме последней
    number = parts[-1]  # Последняя часть - номер

    if card_type in card_types:
        masked_number = get_mask_card_number(number)  # Используйте функцию маскировки карты
    elif card_type == "Счет":
        masked_number = get_mask_account(number)  # Используйте функцию маскировки счета
    else:
        raise ValueError("Неизвестный тип карты или счета")

    return f"{card_type} {masked_number}"


