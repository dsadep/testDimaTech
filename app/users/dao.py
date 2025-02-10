from sqlalchemy import update
from app.dao.base import BaseDAO
from app.users.models import Users
from app.database import async_session_maker

class UsersDAO(BaseDAO):
    model = Users

    @classmethod
    async def update_role(cls, user_id: int, role: str):
        async with async_session_maker() as session:
            query = update(cls.model).filter(cls.model.id == user_id).values(role=role)
            await session.execute(query)
            await session.commit()