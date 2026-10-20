from sqlalchemy.orm import Mapped, mapped_column

from app.database.database import Base

class Subject(Base):
    __tablename__ = "subjects"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    slug: Mapped[str] = mapped_column(unique=True, nullable=False)
    name_ru: Mapped[str] = mapped_column(nullable=False)
    name_tk: Mapped[str] = mapped_column(nullable=False)