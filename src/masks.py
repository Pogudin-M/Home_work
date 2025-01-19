from typing import Optional


def get_mask_card_number(card_number: Optional[str]) -> Optional[str]:
    """Для номера карты показываем только первые 6 цифр и последние 4 цифры, остальные заменяем на звездочки"""
    # Проверяем, что номер карты не None и не пустой
    if card_number is None:
        return ""  # Возвращаем пустую строку для None

    # Удаляем пробелы из номера карты, чтобы избежать ошибок
    card_number = card_number.replace(" ", "")
    # Проверяем, что номер карты достаточно длинный
    if not card_number or len(card_number) < 10:
        return ""  # Возвращаем пустую строку, если номер карты некорректен
    elif len(card_number) <= 12:
        return "**** **** ****"  # Возвращаем маску для коротких номеров

    # Первые 4 цифры остаются видимыми
    first_part = card_number[:4]
    # Следующие 2 цифры остаются видимыми
    second_part = card_number[4:6]
    # Заменяем остальные цифры на звездочки
    masked_part = "*" * (len(card_number) - 14)
    # Последние 4 цифры остаются видимыми
    last_part = card_number[-4:]
    # Формируем итоговую строку
    return f"{first_part} {second_part}{masked_part} **** {last_part}"


def get_mask_account(account_number: Optional[str]) -> Optional[str]:
    """Для номера счета показываем последние 4 цифры, остальные заменяем на звездочки."""

    # Проверяем, что номер счета не None
    if account_number is None:
        return ""  # Возвращаем пустую строку, если номер счета некорректен

    # Если длина номера счета меньше 4, возвращаем пустую строку
    if len(account_number) < 20:
        return ""

    # Если длина номера счета больше 4, заменяем все цифры, кроме последних 4, на звездочки
    masked_part = "*" * (len(account_number) - 4)  # Маскируем все, кроме последних 4
    last_part = account_number[-4:]  # Последние 4 цифры остаются видимыми

    return f"{masked_part}{last_part}"  # Формируем итоговую строку
