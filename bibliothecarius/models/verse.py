from sqlalchemy import ForeignKey, Index, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from bibliothecarius.models.base import Base
from bibliothecarius.models.book import Book
from bibliothecarius.models.translation import Translation


class Verse(Base):
    __tablename__ = "verses"
    __table_args__ = (
        Index("ix_verses_book_id", "bookId"),
        Index("ix_verses_translation_id", "translationId"),
        Index(
            "ix_verses_translation_id_book_id_chapter_verse_number",
            "translationId",
            "bookId",
            "chapter",
            "verseNumber",
        ),
    )

    verse_id: Mapped[int] = mapped_column("id", primary_key=True)
    translation_id: Mapped[int] = mapped_column(
        "translationId", Integer, ForeignKey("translations.id"), nullable=False
    )
    book_id: Mapped[str] = mapped_column(
        "bookId", Integer, ForeignKey("books.id"), nullable=False
    )
    chapter: Mapped[str] = mapped_column(Integer, nullable=False)
    verse_number: Mapped[str] = mapped_column("verseNumber", Integer, nullable=False)
    content: Mapped[str] = mapped_column(String, nullable=False)
    title: Mapped[str] = mapped_column(String, nullable=True, default=None)
    said_jesus: Mapped[int] = mapped_column(
        "saidJesus", Integer, nullable=False, default=0
    )

    translation: Mapped["Translation"] = relationship()
    book: Mapped["Book"] = relationship()

    def __repr__(self) -> str:
        return f"{self.book.name} {self.chapter}:{self.verse_number} - {self.content}"
