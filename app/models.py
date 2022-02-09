import enum

from sqlalchemy import (DECIMAL, Column, DateTime, Enum, ForeignKey, Integer,
                        MetaData, String, Table, text)
from sqlalchemy.dialects.postgresql import UUID

metadata = MetaData()

class RoleEnum(enum.Enum):
    admin = 'admin'
    manager = 'manager'


users = Table(
    'users',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(100), nullable=False),
    Column("hashed_password", String()),
    Column('role', Enum(RoleEnum))
)


tokens = Table(
    "tokens",
    metadata,
    Column("id", Integer, primary_key=True),
    Column(
        "token",
        UUID(as_uuid=False),
        server_default=text("uuid_generate_v4()"),
        unique=True,
        nullable=False,
        index=True,
    ),
    Column("expires", DateTime()),
    Column("user_id", ForeignKey("users.id")),
)


rooms = Table(
    'rooms',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('number', Integer, nullable=False),
    Column('price', DECIMAL(7,2), nullable=False),
    Column('number_of_seats', Integer, nullable=False)
)


bookings = Table(
    'bookings', 
    metadata,
    Column('id', Integer, primary_key=True),
    Column('from', DateTime(), nullable=False),
    Column('to', DateTime(), nullable=False),
    Column('room_id', ForeignKey('rooms.id'), nullable=False)
)
