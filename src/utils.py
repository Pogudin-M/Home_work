import json
from typing import Any, Dict, List, Union


def get_transactions(operations_file: str) -> Union[List[Dict[str, Any]], List]:
    """
    Читает данные о транзакциях из JSON-файла.

    Args:
        operations_file: Путь к JSON-файлу (строка).

    Returns:
        Список словарей с данными о транзакциях или пустой список при ошибке.
    """
    try:
        with open(operations_file, "r", encoding="utf-8") as f:
            data = json.load(f)
            if isinstance(data, list):  # Проверка, что загруженные данные - список
                return data
            else:
                print("Ошибка: Загруженные данные не являются списком.")
                return []
    except (json.JSONDecodeError, FileNotFoundError) as e:
        print(f"Ошибка при чтении файла: {e}")
        return []

        return operations_file
