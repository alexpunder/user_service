from sqlalchemy import MetaData
from sqlalchemy.ext.asyncio import create_async_engine

from src.config import settings
from src.constants import DB_NAMING_CONVENTION

engine = create_async_engine(
    url=settings.db_settings.DSN,
)
metadata = MetaData(
    naming_convention=DB_NAMING_CONVENTION,
)
