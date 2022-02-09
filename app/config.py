from functools import lru_cache

from pydantic import BaseSettings


class DBSettings(BaseSettings):
    user: str
    database: str
    password: str
    host: str
    port: str

    class Config:
        env_prefix = "DB_"
        env_file = ".env"


@lru_cache()
def get_db_settings() -> DBSettings:
    return DBSettings()
