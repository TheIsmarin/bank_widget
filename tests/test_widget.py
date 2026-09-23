"""Тесты для модуля widget."""

import pytest

from src.widget import get_date, mask_account_card


class TestMaskAccountCard:
    """Тесты для mask_account_card."""

    def test_card(self):
        result = mask_account_card("Visa Platinum 7000792289606361")
        assert result == "Visa Platinum 7000 79** **** 6361"

    def test_account(self):
        result = mask_account_card("Счет 73654108430135874305")
        assert result == "Счет **4305"

    def test_invalid_empty(self):
        result = mask_account_card("")
        assert result == "Некорректный ввод"

    def test_invalid_no_number(self):
        result = mask_account_card("Visa")
        assert result == "Некорректный ввод"

    def test_invalid_not_digit(self):
        result = mask_account_card("Visa abc")
        assert result == "Некорректный ввод"


class TestGetDate:
    """Тесты для get_date."""

    @pytest.mark.parametrize(
        "iso_date, expected",
        [
            ("2024-03-11T02:26:18.671407", "11.03.2024"),
            ("2019-07-03T18:35:29.512364", "03.07.2019"),
            ("2018-06-30T02:08:58.425572", "30.06.2018"),
        ],
    )
    def test_get_date(self, iso_date, expected):
        assert get_date(iso_date) == expected
