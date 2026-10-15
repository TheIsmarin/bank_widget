"""Модуль для поиска и подсчёта операций."""

import re
from collections import Counter


def process_bank_search(data: list[dict], search: str) -> list[dict]:
    """
    Ищет операции, в описании которых есть заданная строка.

    Аргументы:
        data: Список словарей с транзакциями.
        search: Строка для поиска в описании.

    Возвращает:
        Список словарей с подходящими операциями.
    """
    pattern = re.compile(re.escape(search), re.IGNORECASE)
    result = []
    for operation in data:
        description = operation.get("description", "")
        if pattern.search(description):
            result.append(operation)
    return result


def process_bank_operations(data: list[dict], categories: list) -> dict:
    """
    Подсчитывает количество операций по категориям.

    Аргументы:
        data: Список словарей с транзакциями.
        categories: Список категорий для подсчёта.

    Возвращает:
        Словарь {категория: количество}.
    """
    descriptions = [op.get("description", "") for op in data]
    counter = Counter(descriptions)
    return {cat: counter.get(cat, 0) for cat in categories}
