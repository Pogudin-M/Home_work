def get_mask_card_number(card_number: str) -> str:
    """Для номера карты показываем только первые 6 цифр и последние 4 цифры, остальные заменяем на звездочки"""
    # Первые 4 цифры остаются видимыми
    first_part = card_number[:4]
    # Следующие 2 цифры остаются видимыми
    second_part = card_number[4:6]
    # Заменяем остальные цифры на звездочки
    masked_part = '*' * (len(card_number) - 14)
    # Последние 4 цифры остаются видимыми
    last_part = card_number[-4:]
    # Формируем итоговую строку
    return f"{first_part} {second_part}{masked_part} **** {last_part}"


def get_mask_account(account_number: str) -> str:
    """Для номера счета показываем только последние 4 цифры, остальные заменяем на звездочки"""
    return f"**{account_number[-4:]}"
