"""Основной модуль программы."""

from src.generators import filter_by_currency
from src.processing import filter_by_state, sort_by_date
from src.readers import read_csv_transactions, read_excel_transactions
from src.search import process_bank_search
from src.utils import load_transactions


def _load_transactions(choice: str) -> list[dict]:
    """Загружает транзакции в зависимости от выбора."""
    if choice == "1":
        print("Для обработки выбран JSON-файл.")
        return load_transactions("data/operations.json")
    if choice == "2":
        print("Для обработки выбран CSV-файл.")
        return read_csv_transactions("data/transactions.csv")
    if choice == "3":
        print("Для обработки выбран XLSX-файл.")
        return read_excel_transactions("data/transactions_excel.xlsx")
    print("Некорректный выбор.")
    return []


def _ask_sort_order() -> bool:
    """Спрашивает порядок сортировки, возвращает reverse."""
    print("Отсортировать по возрастанию или по убыванию?")
    order = input().strip().lower()
    return order == "по убыванию"


def _print_transactions(transactions: list[dict]) -> None:
    """Выводит транзакции."""
    print("Распечатываю итоговый список транзакций...")
    print(f"Всего банковских операций в выборке: {len(transactions)}")
    if not transactions:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")
        return
    for t in transactions:
        date = t.get("date", "")[:10]
        description = t.get("description", "")
        amount = (
            t.get("operationAmount", {}).get("amount", "")
            if "operationAmount" in t
            else t.get("amount", "")
        )
        currency = (
            t.get("operationAmount", {}).get("currency", {}).get("name", "")
            if "operationAmount" in t
            else t.get("currency_name", "")
        )
        print(f"{date} {description}")
        print(f"Сумма: {amount} {currency}")
        print()


def main() -> None:
    """Основная логика программы."""
    print("Привет! Добро пожаловать в программу работы с банковскими транзакциями.")
    print("Выберите необходимый пункт меню:")
    print("1. Получить информацию о транзакциях из JSON-файла")
    print("2. Получить информацию о транзакциях из CSV-файла")
    print("3. Получить информацию о транзакциях из XLSX-файла")

    transactions = _load_transactions(input().strip())
    if not transactions:
        return

    # Фильтрация по статусу
    while True:
        print("Введите статус, по которому необходимо выполнить фильтрацию.")
        print("Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING")
        status = input().strip().upper()
        if status in ("EXECUTED", "CANCELED", "PENDING"):
            break
        print(f'Статус операции "{status}" недоступен.')

    transactions = filter_by_state(transactions, status)
    print(f'Операции отфильтрованы по статусу "{status}"')

    # Сортировка
    print("Отсортировать операции по дате? Да/Нет")
    if input().strip().lower() == "да":
        reverse = _ask_sort_order()
        transactions = sort_by_date(transactions, reverse=reverse)

    # Фильтрация рублёвых
    print("Выводить только рублевые транзакции? Да/Нет")
    if input().strip().lower() == "да":
        transactions = list(filter_by_currency(transactions, "RUB"))

    # Фильтрация по слову
    print("Отфильтровать список транзакций по определенному слову в описании? Да/Нет")
    if input().strip().lower() == "да":
        word = input("Введите слово: ").strip()
        transactions = process_bank_search(transactions, word)

    # Вывод
    _print_transactions(transactions)


if __name__ == "__main__":
    main()
