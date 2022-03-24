from functools import lru_cache

from pydantic import BaseSettings


class Settings(BaseSettings):
    db_user: str
    db_database: str
    db_password: str
    db_host: str
    db_port: str
    jwt_secret_key: str
    jwt_algorithm: str
    jwt_expire_minutes: int

    class Config:
        env_file = ".env"


@lru_cache
def get_settings():
    return Settings()


settings = get_settings()
