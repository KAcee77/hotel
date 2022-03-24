from datetime import datetime, timedelta

from app.models import CreateUser, Token, User
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from passlib.hash import bcrypt
from pydantic import ValidationError
from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel import select

from ..config import settings
from ..db import get_session
from .base_acions import BaseActions

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='auth/sign-in')


class AuthActions:

    @staticmethod
    def verify_password(password: str, hashed_password: str) -> bool:
        return bcrypt.verify(password, hashed_password)

    @staticmethod
    def hash_password(password: str) -> str:
        return bcrypt.hash(password)

    @staticmethod
    def verify_token(token: str) -> User:
        exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Could not validate credentials',
            headers={'WWW-Authenticate': 'Bearer'},
        )
        try:
            payload = jwt.decode(
                token,
                settings.jwt_secret,
                algorithms=[settings.jwt_algorithm],
            )
        except JWTError:
            raise exception

        user_data = payload.get('user')

        try:
            user = User.parse_obj(user_data)
        except ValidationError:
            raise exception

        return user

    @staticmethod
    async def create_token(user: User) -> Token:
        now = datetime.utcnow()
        payload = {
            'iat': now,
            'nbf': now,
            'exp': now + timedelta(seconds=settings.jwt_expire_minutes),
            'sub': str(user.id),
            'user': user.dict(),
        }
        token = jwt.encode(
            payload,
            settings.jwt_secret_key,
            algorithm=settings.jwt_algorithm,
        )
        return Token(access_token=token)
    
    def __init__(self, session: AsyncSession = Depends(get_session)):
        self.session = session

    async def register_new_user(
        self,
        create_user: CreateUser,
    ) -> Token:
        user = User(
            name=create_user.name,
            hashed_password=self.hash_password(create_user.password)
        )
        user = await BaseActions.create_obj(self.session, user)
        return await self.create_token(user)

    async def authenticate_user(
        self,
        username: str,
        password: str,
    ) -> Token:
        exception = HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Incorrect username or password',
            headers={'WWW-Authenticate': 'Bearer'},
        )

        request = await self.session.execute(
            select(User).where(User.name == username)
        )
        user = request.first()[0]
        if not user:
            raise exception
        if not self.verify_password(password, user.hashed_password):
            raise exception

        return await self.create_token(user)
