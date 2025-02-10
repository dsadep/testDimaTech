from pydantic import BaseModel

class SUserBill(BaseModel):
    id: int
    balance: float