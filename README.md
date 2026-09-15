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
