from sqlalchemy import MetaData
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

from src.constants import DB_NAMING_CONVENTION

metadata = MetaData(
    naming_convention=DB_NAMING_CONVENTION,
)


class Base(DeclarativeBase):
    metadata = metadata


class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True, nullable=False)
    name: Mapped[str] = mapped_column()
    surname: Mapped[str] = mapped_column()
    email: Mapped[str] = mapped_column()
    phone: Mapped[str] = mapped_column()
    is_active: Mapped[bool] = mapped_column(default=True)
    is_blocked: Mapped[bool] = mapped_column(default=False)
    is_superuser: Mapped[bool] = mapped_column(default=False)
