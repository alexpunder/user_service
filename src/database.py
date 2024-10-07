from typing import Any, AsyncGenerator

from sqlalchemy.ext.asyncio import (
    AsyncConnection,
    AsyncEngine,
    create_async_engine,
)

from src.config import settings

engine: AsyncEngine = create_async_engine(
    url=settings.db_settings.DSN,
)


async def get_db_connection() -> AsyncGenerator[AsyncConnection, Any]:
    async with engine.connect() as connection:
        try:
            yield connection
        finally:
            await connection.close()
