from bibliothecarius.models.base import Base
from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import String, Integer


class Book(Base):
    __tablename__ = "books"

    id: Mapped[int] = mapped_column(primary_key=True)
    testament: Mapped[str] = mapped_column(String, nullable=False)
    name: Mapped[str] = mapped_column(String, nullable=False)
    abbreviation: Mapped[str] = mapped_column(String, nullable=False)
    totalChapters: Mapped[int] = mapped_column(Integer, default=1)

    def __repr__(self) -> str:
        return f"Book {self.name} - {self.totalChapters} chapters"
