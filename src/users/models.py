from datetime import datetime

from sqlalchemy import MetaData, func
from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

from src.constants import DB_NAMING_CONVENTION

metadata = MetaData(
    naming_convention=DB_NAMING_CONVENTION,
)


class Base(AsyncAttrs, DeclarativeBase):
    __abstract__ = True

    metadata = metadata

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    created_at: Mapped[datetime] = mapped_column(default=func.now())
    updated_at: Mapped[datetime] = mapped_column(
        default=func.now(), onupdate=func.now()
    )


class User(Base):
    __tablename__ = 'users'

    name: Mapped[str]
    surname: Mapped[str | None]
    email: Mapped[str]
    phone_number: Mapped[str]
    avatar: Mapped[str | None]
