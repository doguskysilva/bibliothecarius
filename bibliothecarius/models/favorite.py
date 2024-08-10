from bibliothecarius.models.base import Base
from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy import ForeignKey, Integer

from bibliothecarius.models.book import Book
from bibliothecarius.models.translation import Translation


class Favorite(Base):
    __tablename__ = "favorites"

    favorites_id: Mapped[int] = mapped_column(primary_key=True)
    translation_id: Mapped[int] = mapped_column(
        ForeignKey("translations.translation_id")
    )
    book_id: Mapped[int] = mapped_column(ForeignKey("books.book_id"))
    chapter: Mapped[int] = mapped_column(Integer, nullable=False, default=1)
    verse: Mapped[int] = mapped_column(Integer, nullable=False, default=1)
    content: Mapped[str] = mapped_column(Integer, nullable=False)
    created_at: Mapped[int] = mapped_column(Integer, nullable=False)
    updated_at: Mapped[int] = mapped_column(Integer, nullable=False)

    translation: Mapped["Translation"] = relationship()
    book: Mapped["Book"] = relationship()
