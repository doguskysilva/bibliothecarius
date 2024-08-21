from sqlalchemy import Boolean, ForeignKey, Integer, String
from sqlalchemy.orm import mapped_column, Mapped, relationship

from bibliothecarius.models.base import Base
from bibliothecarius.models.book import Book
from bibliothecarius.models.translation import Translation


class Verse(Base):
    __tablename__ = "verses"

    verse_id: Mapped[int] = mapped_column(primary_key=True)
    translation_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("translations.translation_id"), nullable=False
    )
    book_id: Mapped[str] = mapped_column(
        Integer, ForeignKey("books.book_id"), nullable=False
    )
    chapter: Mapped[str] = mapped_column(Integer, nullable=False)
    verse_number: Mapped[str] = mapped_column(Integer, nullable=False)
    content: Mapped[str] = mapped_column(String, nullable=False)
    title: Mapped[str] = mapped_column(String, nullable=True, default=None)
    said_jesus: Mapped[bool] = mapped_column(Boolean, nullable=True, default=False)

    translation: Mapped["Translation"] = relationship()
    book: Mapped["Book"] = relationship()

    def __repr__(self) -> str:
        return f"{self.book.name} {self.chapter}:{self.verse_number} - {self.content}"
