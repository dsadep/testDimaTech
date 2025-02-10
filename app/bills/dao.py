from sqlalchemy import delete, select, update
from app.bills.models import Bills
from app.dao.base import BaseDAO
from app.database import async_session_maker

class BillsDAO(BaseDAO):
    model = Bills

    @classmethod
    async def delete_by_user_id(cls, user_id: int):
        async with async_session_maker() as session:
            query = delete(Bills).where(Bills.user_id == user_id)
            await session.execute(query)
            await session.commit()

    @classmethod
    async def update_amount(cls, bill_id: int, amount: float):
        async with async_session_maker() as session:
            query = update(Bills).where(Bills.id == bill_id).values(balance=Bills.balance + amount)
            await session.execute(query)
            await session.commit()