"""Модуль для работы с JSON-файлами."""

import json


def load_transactions(file_path: str) -> list[dict]:
    """
    Загружает транзакции из JSON-файла.

    Аргументы:
        file_path: Путь к JSON-файлу.

    Возвращает:
        Список словарей с транзакциями или пустой список.
    """
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        if not isinstance(data, list):
            return []
        return data
    except (FileNotFoundError, json.JSONDecodeError):
        return []
