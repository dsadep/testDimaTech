from hashlib import sha256
from fastapi import APIRouter, HTTPException
from app.bills.dao import BillsDAO
from app.exceptions import InvalidSignatureException, TransactionAlreadyExistsException
from app.payments.schemas import SWebhookData
from app.config import settings
from app.payments.dao import TransactionsDAO
router = APIRouter(
    prefix="/webhook",  
    tags=["Вебхуки"],  
)

@router.post("/")  
async def webhook(data: SWebhookData):
    secret_key = settings.SIGNATURE_SECRET_KEY
    signature_string = f"{str(data.account_id)}{str(data.amount)}{str(data.transaction_id)}{str(data.user_id)}{secret_key}"
    expected_signature = sha256(signature_string.encode()).hexdigest()
    #Debugging information
    print(f"Expected signature: {expected_signature}")
    print(f"Received signature: {data.signature}")
    if expected_signature != data.signature:
        raise InvalidSignatureException
    
    bill = await BillsDAO.find_one_or_none(id=data.account_id)
    if not bill:
        await BillsDAO.add(id=data.account_id,user_id=data.user_id, balance=0.0)

    existing_transaction = await TransactionsDAO.find_one_or_none(transaction_id=data.transaction_id)
    if existing_transaction:
        raise TransactionAlreadyExistsException
    
    await TransactionsDAO.add(transaction_id=data.transaction_id, amount=data.amount, user_id=data.user_id)
    await BillsDAO.update_amount(data.account_id, data.amount)
    return {"status": "success"}
    
