import hashlib

def generate_signature(bill_id: int, amount: float, transaction_id: int, user_id: int, secret_key: str) -> str:
    """
    Генерирует сигнатуру для вебхука на основе входных данных.

    :param account_id: Идентификатор аккаунта
    :param amount: Сумма транзакции
    :param transaction_id: Идентификатор транзакции
    :param user_id: Идентификатор пользователя
    :param secret_key: Секретный ключ для генерации сигнатуры
    :return: Сгенерированная сигнатура в виде строки
    """
    signature_string = f"{bill_id}{amount}{transaction_id}{user_id}{secret_key}"
    return hashlib.sha256(signature_string.encode()).hexdigest()

# Пример использования

secret_key = "BHwQl0LeyoEXGnIyYpBF5Nj5EUewpBfm8ynfJGn6hOk="
bill_id = 7
amount = 100.0
transaction_id = "cd0-472c-bd36-35660f00132b"
user_id = 4

signature = generate_signature(bill_id, amount, transaction_id, user_id, secret_key)
print("Generated Signature:", signature)