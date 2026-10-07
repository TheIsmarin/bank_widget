"""Модуль для конвертации валют через внешний API."""

import os

import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("EXCHANGE_RATES_API_KEY", "")


def convert_to_rub(transaction: dict) -> float:
    """
    Конвертирует сумму транзакции в рубли.

    Аргументы:
        transaction: Словарь с данными о транзакции.

    Возвращает:
        Сумма транзакции в рублях.
    """
    amount = float(transaction["operationAmount"]["amount"])
    currency = transaction["operationAmount"]["currency"]["code"]

    if currency == "RUB":
        return amount

    if currency in ("USD", "EUR"):
        url = "https://api.apilayer.com/exchangerates_data/convert"
        params = {"amount": amount, "from": currency, "to": "RUB"}
        headers = {"apikey": API_KEY}
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        result = response.json()
        return float(result["result"])

    return amount
