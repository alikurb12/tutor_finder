from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from datetime import datetime, timezone

from app.database.database import Base


class User(Base):
    __tablename__ = "users"

    id : Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    phone_number : Mapped[str] = mapped_column(String(18), unique=True, nullable=False)
    password_hash : Mapped[str] = mapped_column(String(100), nullable=False)
    full_name : Mapped[str] = mapped_column(String(100), nullable=False)
    is_admin: Mapped[bool] = mapped_column(default=False)
    is_active: Mapped[bool] = mapped_column(default=True)
    created_at : Mapped[datetime] = mapped_column(default=datetime.now(timezone.utc))
