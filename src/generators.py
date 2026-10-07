"""Модуль с генераторами для обработки транзакций."""

from typing import Iterator


def filter_by_currency(transactions: list[dict], currency: str) -> Iterator[dict]:
    """Фильтрует транзакции по коду валюты."""
    for transaction in transactions:
        if transaction.get("operationAmount", {}).get("currency", {}).get("code") == currency:
            yield transaction


def transaction_descriptions(transactions: list[dict]) -> Iterator[str]:
    """Возвращает описания транзакций по очереди."""
    for transaction in transactions:
        yield transaction.get("description", "")


def card_number_generator(start: int, stop: int) -> Iterator[str]:
    """Генерирует номера карт в формате XXXX XXXX XXXX XXXX."""
    for number in range(start, stop + 1):
        card_str = f"{number:016d}"
        formatted = " ".join(card_str[i : i + 4] for i in range(0, 16, 4))
        yield formatted
