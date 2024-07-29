from bibliothecarius.models.base import Base
from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import String, Integer


class Canon(Base):
    __tablename__ = "canon"

    canon_id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    tradition: Mapped[str] = mapped_column(String, nullable=False)
    total_books: Mapped[int] = mapped_column(Integer, nullable=False)

    def __repr__(self) -> str:
        return f"{self.name} ({self.tradition} - {self.total_books})"
