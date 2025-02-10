from app.database import Base
from sqlalchemy import Column, Integer, String, ForeignKey

class Transactions(Base):
    __tablename__ = "transactions"  

    id = Column(Integer, primary_key=True, index=True)
    transaction_id = Column(String, unique=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    amount = Column(Integer, nullable=False)