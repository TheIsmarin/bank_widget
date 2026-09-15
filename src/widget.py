from datetime import datetime

from src.masks import get_mask_account, get_mask_card_number


def mask_account_card(account_card_info: str) -> str:
    parts = account_card_info.rsplit(" ", 1)

    if len(parts) != 2:
        return "Некорректный ввод"

    name, number = parts

    if not number.isdigit():
        return "Некорректный ввод"

    if "счет" in name.lower() or "account" in name.lower():
        masked = get_mask_account(number)
    else:
        masked = get_mask_card_number(number)

    return f"{name} {masked}"


def get_date(date_string: str) -> str:
    date_obj = datetime.fromisoformat(date_string)
    return date_obj.strftime("%d.%m.%Y")
