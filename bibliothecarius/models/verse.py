from sqlalchemy import Boolean, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from bibliothecarius.models.base import Base
from bibliothecarius.models.book import Book
from bibliothecarius.models.translation import Translation


class Verse(Base):
    __tablename__ = "verses"

    id: Mapped[int] = mapped_column(primary_key=True)
    translationId: Mapped[int] = mapped_column(
        Integer, ForeignKey("translations.id"), nullable=False
    )
    bookId: Mapped[int] = mapped_column(
        Integer, ForeignKey("books.id"), nullable=False
    )
    chapter: Mapped[int] = mapped_column(Integer, nullable=False)
    verseNumber: Mapped[int] = mapped_column(Integer, nullable=False)
    content: Mapped[str] = mapped_column(String, nullable=False)
    title: Mapped[str] = mapped_column(String, nullable=True, default=None)
    saidJesus: Mapped[int] = mapped_column(Integer, nullable=False, default=0)

    translation: Mapped["Translation"] = relationship()
    book: Mapped["Book"] = relationship()

    def __repr__(self) -> str:
        return f"{self.book.name} {self.chapter}:{self.verseNumber} - {self.content}"
