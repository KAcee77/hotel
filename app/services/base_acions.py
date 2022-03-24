from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel import SQLModel


class BaseActions:

    @staticmethod
    async def create_obj(session: AsyncSession, obj: SQLModel) -> SQLModel:
        session.add(obj)
        await session.commit()
        await session.refresh(obj)
        return obj