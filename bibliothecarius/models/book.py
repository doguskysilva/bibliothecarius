from bibliothecarius.models.base import Base
from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import String, Integer

class Book(Base):
    __tablename__ = "books"

    book_id: Mapped[int] = mapped_column(primary_key=True)
    testament: Mapped[str] = mapped_column(String, nullable=False)
    name: Mapped[str] = mapped_column(String, nullable=False)
    abbreviation: Mapped[str] = mapped_column(String, nullable=False)
    total_chapters: Mapped[int] = mapped_column(Integer, default=1)


    def __repr__(self) -> str:
        return f"Book {self.name} - {self.total_chapters} chapters"
        