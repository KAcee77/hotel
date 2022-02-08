import sqlalchemy

from .config import get_db_settings

settings = get_db_settings()

DATABASE_URL = f"postgresql://{settings.username}:\
{settings.password}@{settings.host}:${settings.port}/{settings.database}"


engine = sqlalchemy.create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)


