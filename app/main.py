from fastapi import FastAPI

from . import api


tags_metadata = [
    {
        'name': 'auth',
        'description': 'Авторизация и регистрация',
    },
    {
        'name': 'hotel',
        'description': 'Управление сущностями отеля',
    },
]

app = FastAPI(
    title='hotel',
    description='Сервис управления отелем',
    version='1.0.0',
    openapi_tags=tags_metadata,
)

app.include_router(api.router)
