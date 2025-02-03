import os

import requests
from dotenv import load_dotenv

load_dotenv("../.env")


def exchange(conversion_file: dict) -> dict[str, float]:
    """Конвертирует сумму из одной валюты в рубли (RUB), используя API для конвертации валют"""
    if conversion_file["operationAmount"]["currency"]["code"] == "RUB":
        return conversion_file["operationAmount"]["amount"]
    else:
        convert_to = "RUB"
        convert_from = conversion_file["operationAmount"]["currency"]["code"]
        amount = conversion_file["operationAmount"]["amount"]
        url = f"https://api.apilayer.com/exchangerates_data/convert?to={convert_to}&from={convert_from}&amount={amount}"

        payload: dict[str, float] = {}
        headers = {"apikey": os.getenv("API_KEY")}

        response = requests.request("GET", url, headers=headers, data=payload)

        result = response.json()["result"]
        return result


if __name__ == "__main__":
    res = exchange(
        {
            "id": 207126257,
            "state": "EXECUTED",
            "date": "2019-07-15T11:47:40.496961",
            "operationAmount": {
                "amount": "92688.46",
                "currency": {"name": "USD", "code": "USD"},
            },
            "description": "Открытие вклада",
            "to": "Счет 35737585785074382265",
        }
    )
    print(res)
