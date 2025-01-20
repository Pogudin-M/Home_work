from src.widget import get_date, mask_account_card


# Тесты для функции mask_account_card
def test_mask_account_card() -> None:
    assert (
        mask_account_card("Visa 1234567812345678") == "Visa 1234 56** **** 5678"
    )  # карта
    assert (
        mask_account_card("Счет 12345678901234567890") == "Счет ****************7890"
    )  # счет
    assert mask_account_card("invalid") == ""


# Тесты для функции get_data
def test_get_date() -> None:
    assert get_date("2023-01-01") == "01.01.2023"
    assert get_date("") == ""
    assert get_date(None) == ""
