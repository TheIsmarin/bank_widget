"""Тесты для модуля processing."""

import pytest

from src.processing import filter_by_state, sort_by_date


@pytest.fixture
def operations():
    """Фикстура с тестовыми операциями."""
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


class TestFilterByState:
    """Тесты для filter_by_state."""

    def test_default_state(self, operations):
        result = filter_by_state(operations)
        assert len(result) == 2
        assert all(op["state"] == "EXECUTED" for op in result)

    def test_canceled_state(self, operations):
        result = filter_by_state(operations, "CANCELED")
        assert len(result) == 2
        assert all(op["state"] == "CANCELED" for op in result)

    def test_no_match(self, operations):
        result = filter_by_state(operations, "PENDING")
        assert result == []

    def test_empty_list(self):
        result = filter_by_state([])
        assert result == []

    @pytest.mark.parametrize(
        "state, expected_count",
        [
            ("EXECUTED", 2),
            ("CANCELED", 2),
            ("PENDING", 0),
        ],
    )
    def test_parametrized(self, operations, state, expected_count):
        result = filter_by_state(operations, state)
        assert len(result) == expected_count


class TestSortByDate:
    """Тесты для sort_by_date."""

    def test_default_descending(self, operations):
        result = sort_by_date(operations)
        dates = [op["date"] for op in result]
        assert dates == sorted(dates, reverse=True)

    def test_ascending(self, operations):
        result = sort_by_date(operations, reverse=False)
        dates = [op["date"] for op in result]
        assert dates == sorted(dates)

    def test_empty_list(self):
        result = sort_by_date([])
        assert result == []

    def test_single_item(self):
        ops = [{"id": 1, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"}]
        result = sort_by_date(ops)
        assert len(result) == 1

    @pytest.mark.parametrize(
        "reverse, expected_first_id",
        [
            (True, 41428829),
            (False, 939719570),
        ],
    )
    def test_parametrized(self, operations, reverse, expected_first_id):
        result = sort_by_date(operations, reverse=reverse)
        assert result[0]["id"] == expected_first_id
