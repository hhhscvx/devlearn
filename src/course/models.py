from sqlalchemy import Integer
from sqlalchemy.orm import Mapped, mapped_column

from src.infrastructure.database import Base


class Course(Base):
    __tablename__ = "courses"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)

    title: Mapped[str]
    description: Mapped[str]
