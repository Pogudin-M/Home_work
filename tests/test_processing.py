from src.processing import filter_by_state, sort_by_date


# Тесты для функции filter_by_state
def test_filter_by_state() -> None:
    data = [
        {"date": "2023-01-01", "state": "EXECUTED"},
        {"date": "2023-01-02", "state": "PENDING"},
        {"date": "2023-01-01", "state": "EXECUTED"},
    ]
    assert filter_by_state(data, "EXECUTED") == [
        {"date": "2023-01-01", "state": "EXECUTED"},
        {"date": "2023-01-01", "state": "EXECUTED"},
    ]
    assert filter_by_state(data, "PENDING") == [
        {"date": "2023-01-02", "state": "PENDING"}
    ]


# Тесты для функции sort_by_date
def test_sort_by_date() -> None:
    data = [{"date": "2023-01-01"}, {"date": "2023-01-02"}]
    assert sort_by_date(data, descending=True) == [
        {"date": "2023-01-02"},
        {"date": "2023-01-01"},
    ]
    assert sort_by_date(data, descending=False) == [
        {"date": "2023-01-01"},
        {"date": "2023-01-02"},
    ]
