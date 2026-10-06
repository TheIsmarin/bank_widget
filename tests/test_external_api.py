"""Тесты для модуля external_api."""

from unittest.mock import Mock, patch

from src.external_api import convert_to_rub


def test_convert_rub():
    """Тест конвертации рублевой транзакции."""
    transaction = {
        "operationAmount": {
            "amount": "1000.00",
            "currency": {"code": "RUB"},
        }
    }
    assert convert_to_rub(transaction) == 1000.0


@patch("src.external_api.requests.get")
def test_convert_usd(mock_get):
    """Тест конвертации USD в RUB."""
    mock_response = Mock()
    mock_response.json.return_value = {"result": 90000.0}
    mock_response.raise_for_status = Mock()
    mock_get.return_value = mock_response

    transaction = {
        "operationAmount": {
            "amount": "1000.00",
            "currency": {"code": "USD"},
        }
    }
    result = convert_to_rub(transaction)
    assert result == 90000.0
    mock_get.assert_called_once()


@patch("src.external_api.requests.get")
def test_convert_eur(mock_get):
    """Тест конвертации EUR в RUB."""
    mock_response = Mock()
    mock_response.json.return_value = {"result": 95000.0}
    mock_response.raise_for_status = Mock()
    mock_get.return_value = mock_response

    transaction = {
        "operationAmount": {
            "amount": "1000.00",
            "currency": {"code": "EUR"},
        }
    }
    result = convert_to_rub(transaction)
    assert result == 95000.0


def test_convert_other_currency():
    """Тест конвертации валюты, не требующей API (например, GBP)."""
    transaction = {
        "operationAmount": {
            "amount": "1000.00",
            "currency": {"code": "GBP"},
        }
    }
    assert convert_to_rub(transaction) == 1000.0
