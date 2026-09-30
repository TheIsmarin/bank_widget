"""Тесты для модуля decorators."""


import pytest

from src.decorators import log


def test_log_to_console_success(capsys):
    """Тест логирования успешного выполнения в консоль."""

    @log()
    def add(x, y):
        return x + y

    result = add(1, 2)
    captured = capsys.readouterr()
    assert result == 3
    assert "add ok" in captured.out


def test_log_to_console_error(capsys):
    """Тест логирования ошибки в консоль."""

    @log()
    def divide(x, y):
        return x / y

    with pytest.raises(ZeroDivisionError):
        divide(1, 0)

    captured = capsys.readouterr()
    assert "divide error" in captured.out
    assert "Inputs: (1, 0), {}" in captured.out


def test_log_to_file_success(tmp_path):
    """Тест логирования успешного выполнения в файл."""
    log_file = tmp_path / "mylog.txt"

    @log(filename=str(log_file))
    def add(x, y):
        return x + y

    add(1, 2)

    content = log_file.read_text(encoding="utf-8")
    assert "add ok" in content


def test_log_to_file_error(tmp_path):
    """Тест логирования ошибки в файл."""
    log_file = tmp_path / "mylog.txt"

    @log(filename=str(log_file))
    def divide(x, y):
        return x / y

    with pytest.raises(ZeroDivisionError):
        divide(1, 0)

    content = log_file.read_text(encoding="utf-8")
    assert "divide error" in content
    assert "Inputs: (1, 0), {}" in content


def test_log_preserves_function_metadata():
    """Тест сохранения метаданных функции."""

    @log()
    def my_func(x):
        """Docstring."""
        return x

    assert my_func.__name__ == "my_func"
    assert my_func.__doc__ == "Docstring."
