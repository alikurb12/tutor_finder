from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Column, ForeignKey, String, Table, Text
from app.database.database import Base
from app.models.subject import Subject


tutor_subjects = Table(
    "tutor_subjects",
    Base.metadata,
    Column("tutor_id", ForeignKey("tutors.id", ondelete="CASCADE"), primary_key=True),
    Column("subject_id", ForeignKey("subjects.id", ondelete="CASCADE"), primary_key=True),
)

class Tutor(Base):
    __tablename__ = "tutors"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"), unique=True, nullable=False)
    experience: Mapped[int] = mapped_column(nullable=False)
    education: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[str] = mapped_column(Text())
    price_per_lesson: Mapped[int] = mapped_column(nullable=False)

    user: Mapped["User"] = relationship(back_populates="tutor") # type: ignore
    subjects: Mapped[list[Subject]] = relationship(secondary=tutor_subjects)