from app.models.hotel import CreateRoom, Room
from fastapi import Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel import select

from ..db import get_session
from .base_acions import BaseActions


class RoomActions:
    def __init__(self, session: AsyncSession = Depends(get_session)):
        self.session = session

    async def create(self, room: CreateRoom) -> Room:
        request = await self.session.execute(
            select(Room).where(Room.number == room.number)
        )
        room_already = request.first()
        if room_already:
            raise HTTPException(
                status_code=409, detail="This number room already exist"
            )
        room = await BaseActions.create_obj(self.session, Room.from_orm(room))
        return room


class BookingActions:
    pass

