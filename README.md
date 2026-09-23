# Bank Widget

Виджет банковских операций клиента.

## Модули

### `src/masks.py`
- `get_mask_card_number` — маскировка номера карты (XXXX XX** **** XXXX)
- `get_mask_account` — маскировка номера счета (**XXXX)

### `src/widget.py`
- `mask_account_card` — универсальная маскировка карты или счета
- `get_date` — преобразование даты из ISO в ДД.ММ.ГГГГ

### `src/processing.py`
- `filter_by_state` — фильтрация операций по статусу
- `sort_by_date` — сортировка операций по дате

### `src/generators.py`
- `filter_by_currency` — фильтрация транзакций по валюте
- `transaction_descriptions` — описания транзакций
- `card_number_generator` — генерация номеров карт

## Установка

1. Клонируйте репозиторий:
git clone https://github.com/TheIsmarin/bank_widget.git
2. Установите зависимости:
poetry install

## Примеры использования

```python
from src.masks import get_mask_card_number, get_mask_account
from src.widget import mask_account_card, get_date
from src.processing import filter_by_state, sort_by_date
from src.generators import (
    filter_by_currency,
    transaction_descriptions,
    card_number_generator,
)

# Маскировка карты и счета
print(get_mask_card_number("7000792289606361"))  # 7000 79** **** 6361
print(get_mask_account("73654108430135874305"))  # **4305
print(mask_account_card("Visa Platinum 7000792289606361"))  # Visa Platinum 7000 79** **** 6361
print(mask_account_card("Счет 73654108430135874305"))  # Счет **4305

# Работа с датой
print(get_date("2024-03-11T02:26:18.671407"))  # 11.03.2024

# Фильтрация и сортировка операций
operations = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
]
print(filter_by_state(operations))  # только EXECUTED
print(sort_by_date(operations))     # отсортировано по дате

# Генераторы
transactions = [
    {
        "id": 939719570,
        "operationAmount": {"currency": {"code": "USD"}},
        "description": "Перевод организации",
    },
]
usd = filter_by_currency(transactions, "USD")
print(next(usd))  # транзакция в USD

for card in card_number_generator(1, 3):
    print(card)
# 0000 0000 0000 0001
# 0000 0000 0000 0002
# 0000 0000 0000 0003