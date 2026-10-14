"""Основной модуль программы."""

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


def _filter_by_status(transactions: list[dict]) -> list[dict]:
    """Фильтрует по статусу."""
    while True:
        print("Введите статус, по которому необходимо выполнить фильтрацию.")
        print("Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING")
        status = input().strip().upper()
        if status in ("EXECUTED", "CANCELED", "PENDING"):
            break
        print(f'Статус операции "{status}" недоступен.')
    result = [t for t in transactions if t.get("state") == status]
    print(f'Операции отфильтрованы по статусу "{status}"')
    return result


def _sort_by_date(transactions: list[dict]) -> list[dict]:
    """Сортирует по дате."""
    print("Отсортировать операции по дате? Да/Нет")
    if input().strip().lower() == "да":
        print("Отсортировать по возрастанию или по убыванию?")
        order = input().strip().lower()
        reverse = order == "по убыванию"
        transactions.sort(key=lambda t: t.get("date", ""), reverse=reverse)
    return transactions


def _filter_rub(transactions: list[dict]) -> list[dict]:
    """Фильтрует только рублёвые транзакции."""
    print("Выводить только рублевые транзакции? Да/Нет")
    if input().strip().lower() == "да":
        return [t for t in transactions if t.get("operationAmount", {}).get("currency", {}).get("code") == "RUB"]
    return transactions


def _filter_by_word(transactions: list[dict]) -> list[dict]:
    """Фильтрует по слову в описании."""
    print("Отфильтровать список транзакций по определенному слову в описании? Да/Нет")
    if input().strip().lower() == "да":
        word = input("Введите слово: ").strip()
        return process_bank_search(transactions, word)
    return transactions


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
        amount = t.get("operationAmount", {}).get("amount", "")
        currency = t.get("operationAmount", {}).get("currency", {}).get("name", "")
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

    transactions = _filter_by_status(transactions)
    transactions = _sort_by_date(transactions)
    transactions = _filter_rub(transactions)
    transactions = _filter_by_word(transactions)
    _print_transactions(transactions)


if __name__ == "__main__":
    main()
