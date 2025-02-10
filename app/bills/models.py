from sqlalchemy import Column, Float, ForeignKey, Integer
from app.database import Base

class Bills(Base):
    __tablename__ = "bills"

    id = Column(Integer, primary_key=True, index=True)
    balance = Column(Float, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))