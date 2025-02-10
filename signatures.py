import hashlib

def generate_signature(bill_id: int, amount: float, transaction_id: int, user_id: int, secret_key: str) -> str:
    signature_string = f"{bill_id}{amount}{transaction_id}{user_id}{secret_key}"
    return hashlib.sha256(signature_string.encode()).hexdigest()

"""
Helping file to generate signature for the payment gateway.
"""

secret_key = "your_secret_key"
bill_id = 0
amount = 0.0
transaction_id = "transaction_id"
user_id = 0

signature = generate_signature(bill_id, amount, transaction_id, user_id, secret_key)
print("Generated Signature:", signature)