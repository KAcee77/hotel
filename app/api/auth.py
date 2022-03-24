from app.services.auth import AuthActions
from fastapi import APIRouter, Depends, status
from fastapi.security import OAuth2PasswordRequestForm

from .. import models
from ..services.auth import AuthActions

router = APIRouter(
    prefix='/auth',
    tags=['auth'],
)


@router.post(
    '/sign-up/',
    response_model=models.Token,
    status_code=status.HTTP_201_CREATED,
)
async def sign_up(
    user_data: models.CreateUser,
    auth_actions: AuthActions = Depends(),
):
    return await auth_actions.register_new_user(user_data)


@router.post(
    '/sign-in/',
    response_model=models.Token,
)
async def sign_in(
    auth_data: OAuth2PasswordRequestForm = Depends(),
    auth_actions: AuthActions = Depends(),
):
    return await auth_actions.authenticate_user(
        auth_data.username,
        auth_data.password,
    )

