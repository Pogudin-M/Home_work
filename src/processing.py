def filter_by_state(data: list, state: str = "EXECUTED") -> list:

    """
    Фильтрует список словарей по значению ключа 'state'.

    :param data: список словарей для фильтрации.
    :param state: значение, по которому будет происходить фильтрация (по умолчанию 'EXECUTED').
    :return: новый список словарей с указанным значением ключа 'state'.
    """
    filtered_data = []  # Создаем пустой список для хранения отфильтрованных данных

    for item in data:  # Проходим по каждому словарю в списке
        if (
            item.get("state") == state
        ):  # Проверяем, соответствует ли значение 'state' заданному
            filtered_data.append(
                item
            )  # Если соответствует, добавляем словарь в новый список

    return filtered_data  # Возвращаем отфильтрованный список


def sort_by_date(data: list, descending: bool = True) -> list:

    """
    Сортирует список словарей по значению ключа 'date'.

    :param data: список словарей для сортировки.
    :param descending: порядок сортировки (по умолчанию True для убывания).
    :return: новый список словарей, отсортированный по дате.
    """
    # Создаем новый список, чтобы не изменять оригинальный
    sorted_data = []
    # Сначала создаем список дат
    dates = [item["date"] for item in data]

    # Сортируем даты
    dates.sort(reverse=descending)

    # Проходим по отсортированным датам и собираем словари
    for date in dates:
        for item in data:
            if item["date"] == date:
                sorted_data.append(item)
                break  # Прерываем внутренний цикл, чтобы не добавлять один и тот же словарь несколько раз

    return sorted_data  # Возвращаем отсортированный список
