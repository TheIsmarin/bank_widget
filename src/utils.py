"""Модуль для работы с JSON-файлами."""

import json
import logging
import os

os.makedirs("logs", exist_ok=True)

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler("logs/utils.log", mode="w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


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
            logger.error(f"JSON не является списком: {file_path}")
            return []
        logger.info(f"Успешно загружено {len(data)} транзакций из {file_path}")
        return data
    except FileNotFoundError:
        logger.error(f"Файл не найден: {file_path}")
        return []
    except json.JSONDecodeError:
        logger.error(f"Ошибка декодирования JSON: {file_path}")
        return []
