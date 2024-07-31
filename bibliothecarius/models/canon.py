from typing import List
from bibliothecarius.models.base import Base
from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy import Column, ForeignKey, String, Integer, Table
from bibliothecarius.models.book import Book


associative_table = Table(
    "book_canon",
    Base.metadata,
    Column("canon_id", ForeignKey("canons.canon_id")),
    Column("book_id", ForeignKey("books.book_id")),
    Column("sort_index", Integer)
)


class Canon(Base):
    __tablename__ = "canons"

    canon_id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    tradition: Mapped[str] = mapped_column(String, nullable=False)
    total_books: Mapped[int] = mapped_column(Integer, nullable=False)

    books: Mapped[List[Book]] = relationship(secondary=associative_table)

    def __repr__(self) -> str:
        return f"{self.name} ({self.tradition} - {self.total_books})"
