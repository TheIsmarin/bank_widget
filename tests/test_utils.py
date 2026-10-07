"""Тесты для модуля utils."""

import json

from src.utils import load_transactions


def test_load_transactions_success(tmp_path):
    """Тест загрузки существующего файла."""
    file = tmp_path / "test.json"
    data = [{"id": 1, "amount": 100}]
    file.write_text(json.dumps(data), encoding="utf-8")

    result = load_transactions(str(file))
    assert result == data


def test_load_transactions_not_found():
    """Тест загрузки несуществующего файла."""
    result = load_transactions("nonexistent.json")
    assert result == []


def test_load_transactions_invalid_json(tmp_path):
    """Тест загрузки некорректного JSON."""
    file = tmp_path / "bad.json"
    file.write_text("not a json", encoding="utf-8")

    result = load_transactions(str(file))
    assert result == []


def test_load_transactions_not_list(tmp_path):
    """Тест загрузки JSON, который не является списком."""
    file = tmp_path / "dict.json"
    file.write_text('{"key": "value"}', encoding="utf-8")

    result = load_transactions(str(file))
    assert result == []


def test_load_transactions_empty_file(tmp_path):
    """Тест загрузки пустого файла."""
    file = tmp_path / "empty.json"
    file.write_text("[]", encoding="utf-8")

    result = load_transactions(str(file))
    assert result == []
