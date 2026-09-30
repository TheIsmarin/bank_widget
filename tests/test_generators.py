"""Тесты для модуля generators."""

import pytest

from src.generators import (
    card_number_generator,
    filter_by_currency,
    transaction_descriptions,
)


@pytest.fixture
def transactions():
    """Фикстура с тестовыми транзакциями."""
    return [
        {
            "id": 939719570,
            "operationAmount": {"currency": {"code": "USD"}},
            "description": "Перевод организации",
        },
        {
            "id": 142264268,
            "operationAmount": {"currency": {"code": "USD"}},
            "description": "Перевод со счета на счет",
        },
        {
            "id": 873106923,
            "operationAmount": {"currency": {"code": "RUB"}},
            "description": "Перевод со счета на счет",
        },
        {
            "id": 895315941,
            "operationAmount": {"currency": {"code": "USD"}},
            "description": "Перевод с карты на карту",
        },
    ]


class TestFilterByCurrency:
    """Тесты для filter_by_currency."""

    def test_filter_usd(self, transactions):
        result = list(filter_by_currency(transactions, "USD"))
        assert len(result) == 3
        assert all(
            t["operationAmount"]["currency"]["code"] == "USD" for t in result
        )

    def test_filter_rub(self, transactions):
        result = list(filter_by_currency(transactions, "RUB"))
        assert len(result) == 1
        assert result[0]["id"] == 873106923

    def test_filter_no_match(self, transactions):
        result = list(filter_by_currency(transactions, "EUR"))
        assert result == []

    def test_filter_empty_list(self):
        result = list(filter_by_currency([], "USD"))
        assert result == []

    def test_returns_iterator(self, transactions):
        result = filter_by_currency(transactions, "USD")
        assert hasattr(result, "__next__")


class TestTransactionDescriptions:
    """Тесты для transaction_descriptions."""

    def test_all_descriptions(self, transactions):
        result = list(transaction_descriptions(transactions))
        assert result == [
            "Перевод организации",
            "Перевод со счета на счет",
            "Перевод со счета на счет",
            "Перевод с карты на карту",
        ]

    def test_empty_list(self):
        result = list(transaction_descriptions([]))
        assert result == []

    def test_first_descriptions(self, transactions):
        gen = transaction_descriptions(transactions)
        assert next(gen) == "Перевод организации"
        assert next(gen) == "Перевод со счета на счет"


class TestCardNumberGenerator:
    """Тесты для card_number_generator."""

    @pytest.mark.parametrize(
        "start, stop, expected_first, expected_last",
        [
            (1, 1, "0000 0000 0000 0001", "0000 0000 0000 0001"),
            (1, 3, "0000 0000 0000 0001", "0000 0000 0000 0003"),
            (100, 102, "0000 0000 0000 0100", "0000 0000 0000 0102"),
        ],
    )
    def test_range(self, start, stop, expected_first, expected_last):
        result = list(card_number_generator(start, stop))
        assert result[0] == expected_first
        assert result[-1] == expected_last
        assert len(result) == stop - start + 1

    def test_format(self):
        result = list(card_number_generator(1, 1))
        assert result[0] == "0000 0000 0000 0001"
        assert len(result[0]) == 19

    def test_returns_generator(self):
        result = card_number_generator(1, 5)
        assert hasattr(result, "__next__")