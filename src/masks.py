"""Модуль для маскировки номеров карт и счетов."""

import logging
import os

os.makedirs("logs", exist_ok=True)

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler("logs/masks.log", mode="w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_mask_card_number(card_number: str) -> str:
    """Маскирует номер банковской карты в формате XXXX XX** **** XXXX."""
    number = card_number.replace(" ", "")
    if len(number) != 16 or not number.isdigit():
        logger.error(f"Некорректный номер карты: {card_number}")
        return card_number
    logger.info(f"Номер карты замаскирован: {card_number}")
    return f"{number[:4]} {number[4:6]}** **** {number[12:]}"


def get_mask_account(account_number: str) -> str:
    """Маскирует номер банковского счета в формате **XXXX."""
    number = account_number.replace(" ", "")
    if len(number) < 4 or not number.isdigit():
        logger.error(f"Некорректный номер счета: {account_number}")
        return account_number
    logger.info(f"Номер счета замаскирован: {account_number}")
    return f"**{number[-4:]}"
