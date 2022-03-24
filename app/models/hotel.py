from datetime import datetime
from typing import Optional

from pydantic import condecimal
from sqlmodel import Field, SQLModel, UniqueConstraint


class BaseRoom(SQLModel):
    number: int
    price: condecimal(max_digits=7, decimal_places=2)
    number_of_seats: int


class Room(BaseRoom, table=True):
    __table_args__ = (UniqueConstraint("number"),)
    id: Optional[int] = Field(default=None, primary_key=True)


class CreateRoom(BaseRoom):
    pass


class BaseBooking(SQLModel):
    start: datetime
    end: datetime
    room_id: int = Field(foreign_key='room.id')


class Booking(BaseBooking, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)


class CreateBooking(BaseBooking):
    pass
