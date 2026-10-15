"""Тесты для модуля search."""

from src.search import process_bank_operations, process_bank_search


def test_process_bank_search():
    data = [
        {"description": "Перевод организации"},
        {"description": "Перевод с карты на карту"},
        {"description": "Открытие вклада"},
    ]
    result = process_bank_search(data, "Перевод")
    assert len(result) == 2


def test_process_bank_search_empty():
    result = process_bank_search([], "Перевод")
    assert result == []


def test_process_bank_operations():
    data = [
        {"description": "Перевод организации"},
        {"description": "Перевод организации"},
        {"description": "Открытие вклада"},
    ]
    result = process_bank_operations(data, ["Перевод организации", "Открытие вклада"])
    assert result == {"Перевод организации": 2, "Открытие вклада": 1}


def test_process_bank_operations_empty():
    result = process_bank_operations([], ["Перевод"])
    assert result == {"Перевод": 0}
