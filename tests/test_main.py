"""Тесты для модуля main."""

from unittest.mock import patch

from src.main import main


@patch("builtins.input", side_effect=["1", "EXECUTED", "нет", "нет", "нет"])
@patch("src.main.load_transactions", return_value=[])
def test_main_json_empty(mock_load, mock_input):
    """Тест main с JSON и пустым списком."""
    main()
    mock_load.assert_called_once()


@patch("builtins.input", side_effect=["2", "EXECUTED", "нет", "нет", "нет"])
@patch("src.main.read_csv_transactions", return_value=[])
def test_main_csv_empty(mock_read, mock_input):
    """Тест main с CSV и пустым списком."""
    main()
    mock_read.assert_called_once()


@patch("builtins.input", side_effect=["3", "EXECUTED", "нет", "нет", "нет"])
@patch("src.main.read_excel_transactions", return_value=[])
def test_main_excel_empty(mock_read, mock_input):
    """Тест main с Excel и пустым списком."""
    main()
    mock_read.assert_called_once()


@patch("builtins.input", side_effect=["4"])
def test_main_invalid_choice(mock_input):
    """Тест main с некорректным выбором."""
    main()


@patch("builtins.input", side_effect=["1", "EXECUTED", "да", "по возрастанию", "да", "нет"])
@patch("src.main.load_transactions")
def test_main_full_flow(mock_load, mock_input):
    """Тест полного потока с транзакциями."""
    mock_load.return_value = [
        {
            "date": "2019-07-03T18:35:29.512364",
            "state": "EXECUTED",
            "description": "Перевод организации",
            "operationAmount": {
                "amount": "1000.00",
                "currency": {"code": "RUB", "name": "руб."},
            },
        }
    ]
    main()


@patch("builtins.input", side_effect=["1", "test", "EXECUTED", "нет", "нет", "нет"])
@patch("src.main.load_transactions", return_value=[])
def test_main_invalid_status(mock_load, mock_input):
    """Тест main с некорректным статусом."""
    main()


@patch("builtins.input", side_effect=["1", "EXECUTED", "нет", "нет", "да", "Перевод"])
@patch("src.main.load_transactions")
def test_main_filter_by_word(mock_load, mock_input):
    """Тест main с фильтрацией по слову."""
    mock_load.return_value = [
        {
            "date": "2019-07-03T18:35:29.512364",
            "state": "EXECUTED",
            "description": "Перевод организации",
            "operationAmount": {
                "amount": "1000.00",
                "currency": {"code": "RUB", "name": "руб."},
            },
        }
    ]
    main()
