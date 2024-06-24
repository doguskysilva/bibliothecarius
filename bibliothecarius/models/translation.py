from bibliothecarius.models.base import Base
from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import String, Integer


class Translation(Base):
    __tablename__ = "translations"

    translation_id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String, nullable=False)
    description: Mapped[str] = mapped_column(String, nullable=False)
    abbreviation: Mapped[str] = mapped_column(String, nullable=False)
    language: Mapped[str] = mapped_column(String, nullable=False)
    country: Mapped[str] = mapped_column(String, nullable=False)
    total_books: Mapped[int] = mapped_column(Integer, nullable=False)
    total_verses: Mapped[int] = mapped_column(Integer, nullable=False)

    def __repr__(self) -> str:
        return f"{self.name} ({self.language} - {self.country})"
