import enum
from typing import Optional

from sqlmodel import Field, SQLModel, UniqueConstraint


class RoleEnum(str, enum.Enum):
    admin = 'admin'
    manager = 'manager'


class BaseUser(SQLModel):
    name: str


class User(BaseUser, table=True):
    __table_args__ = (UniqueConstraint("name"),)
    id: Optional[int] = Field(default=None, primary_key=True)
    role: RoleEnum = Field(default=RoleEnum.manager)
    hashed_password: str


class CreateUser(BaseUser):
    password: str


class Token(SQLModel):
    access_token: str
    token_type: str = 'bearer'
