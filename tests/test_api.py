from unittest.mock import patch

from src.api import exchange


@patch("requests.request")
def test_exchange(mock_get):
    mock_get.return_value.json.return_value = {"result": 9245001.337534}
    assert (
        exchange(
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
        == 9245001.337534
    )
