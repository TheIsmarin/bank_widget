"""Тесты для модуля readers."""

from unittest.mock import MagicMock, patch

from src.readers import read_csv_transactions, read_excel_transactions


@patch("src.readers.pd.read_csv")
def test_read_csv_transactions(mock_read_csv):
    """Тест чтения CSV."""
    mock_df = MagicMock()
    mock_df.to_dict.return_value = [{"id": 1, "amount": 100}]
    mock_read_csv.return_value = mock_df

    result = read_csv_transactions("data/transactions.csv")
    assert result == [{"id": 1, "amount": 100}]
    mock_read_csv.assert_called_once_with("data/transactions.csv", sep=";")


@patch("src.readers.pd.read_csv")
def test_read_csv_transactions_not_found(mock_read_csv):
    """Тест чтения несуществующего CSV."""
    mock_read_csv.side_effect = FileNotFoundError()

    result = read_csv_transactions("nonexistent.csv")
    assert result == []


@patch("src.readers.pd.read_csv")
def test_read_csv_transactions_error(mock_read_csv):
    """Тест чтения CSV с ошибкой."""
    mock_read_csv.side_effect = Exception("Some error")

    result = read_csv_transactions("bad.csv")
    assert result == []


@patch("src.readers.pd.read_excel")
def test_read_excel_transactions_error(mock_read_excel):
    """Тест чтения Excel с ошибкой."""
    mock_read_excel.side_effect = Exception("Some error")

    result = read_excel_transactions("bad.xlsx")
    assert result == []


@patch("src.readers.pd.read_excel")
def test_read_excel_transactions(mock_read_excel):
    """Тест чтения Excel."""
    mock_df = MagicMock()
    mock_df.to_dict.return_value = [{"id": 1, "amount": 100}]
    mock_read_excel.return_value = mock_df

    result = read_excel_transactions("data/transactions_excel.xlsx")
    assert result == [{"id": 1, "amount": 100}]
    mock_read_excel.assert_called_once_with("data/transactions_excel.xlsx")


@patch("src.readers.pd.read_excel")
def test_read_excel_transactions_not_found(mock_read_excel):
    """Тест чтения несуществующего Excel."""
    mock_read_excel.side_effect = FileNotFoundError()

    result = read_excel_transactions("nonexistent.xlsx")
    assert result == []
