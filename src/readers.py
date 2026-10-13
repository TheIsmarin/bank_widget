"""Модуль для чтения данных из CSV и Excel файлов."""

import pandas as pd


def read_csv_transactions(file_path: str) -> list[dict]:
    """
    Читает транзакции из CSV-файла.

    Аргументы:
        file_path: Путь к CSV-файлу.

    Возвращает:
        Список словарей с транзакциями.
    """
    try:
        df = pd.read_csv(file_path, sep=";")
        result: list[dict] = df.to_dict(orient="records")
        return result
    except FileNotFoundError:
        return []
    except Exception:
        return []


def read_excel_transactions(file_path: str) -> list[dict]:
    """
    Читает транзакции из Excel-файла.

    Аргументы:
        file_path: Путь к Excel-файлу.

    Возвращает:
        Список словарей с транзакциями.
    """
    try:
        df = pd.read_excel(file_path)
        result: list[dict] = df.to_dict(orient="records")
        return result
    except FileNotFoundError:
        return []
    except Exception:
        return []