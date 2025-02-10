from pydantic import BaseModel

class SWebhookData(BaseModel):
    transaction_id: str
    account_id: int
    user_id: int
    amount: float
    signature: str

class SUserTransactions(BaseModel):
    amount: float
    transaction_id: str