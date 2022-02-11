import enum
import uuid as uuid_pkg
from datetime import datetime

from pydantic import condecimal
from sqlmodel import Field, SQLModel


class RoleEnum(str, enum.Enum):
    admin = 'admin'
    manager = 'manager'


class User(SQLModel, table=True):
    id: int = Field(primary_key=True)
    name: str
    hashed_password: str
    role: RoleEnum


class Token(SQLModel, table=True):
    id: int = Field(primary_key=True)
    expires: datetime
    uuid: uuid_pkg.UUID = Field(
        default_factory=uuid_pkg.uuid4,
        index=True
    )
    user_id: int = Field(foreign_key='user.id')


class Room(SQLModel, table=True):
    id: int = Field(primary_key=True)
    number: int
    price: condecimal(max_digits=7, decimal_places=2)
    number_of_seats: int


class Booking(SQLModel, table=True):
    id: int = Field(primary_key=True)
    start: datetime
    end: datetime
    room_id: int = Field(foreign_key='room.id')

