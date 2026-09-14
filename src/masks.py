def get_mask_card_number(card_number: str) -> str:
    number = card_number.replace(" ", "")
    if len(number) != 16 or not number.isdigit():
        return card_number
    return f"{number[:4]} {number[4:6]}** **** {number[12:]}"


def get_mask_account(account_number: str) -> str:
    number = account_number.replace(" ", "")
    if len(number) < 4 or not number.isdigit():
        return account_number
    return f"**{number[-4:]}"
