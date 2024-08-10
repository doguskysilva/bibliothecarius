from typing import List
from bibliothecarius.models.base import Base
from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy import ForeignKey, String, Integer
from bibliothecarius.models.book import Book


class BookCanon(Base):
    __tablename__ = "book_canon"
    
    book_canon_id: Mapped[int] = mapped_column(primary_key=True) 
    canon_id: Mapped[int] = mapped_column(ForeignKey("canons.canon_id"))
    book_id: Mapped[int] = mapped_column(ForeignKey("books.book_id"))
    sort_index: Mapped[int]
    book: Mapped["Book"] = relationship()

    def __repr__(self) -> str:
        return f"{self.book.name} - {self.sort_index}"


class Canon(Base):
    __tablename__ = "canons"

    canon_id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    tradition: Mapped[str] = mapped_column(String, nullable=False)
    total_books: Mapped[int] = mapped_column(Integer, nullable=False)

    books: Mapped[List["BookCanon"]] = relationship()

    def __repr__(self) -> str:
        return f"{self.name} ({self.tradition} - {self.total_books})"
