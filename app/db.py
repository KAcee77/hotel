import databases

from .config import get_db_settings


settings = get_db_settings()

DATABASE_URL = f"postgresql://{settings.user}:\
{settings.password}@{settings.host}:${settings.port}/{settings.database}"

database = databases.Database(DATABASE_URL)

