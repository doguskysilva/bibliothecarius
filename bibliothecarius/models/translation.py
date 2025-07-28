from sqlalchemy import ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from bibliothecarius.models.base import Base
from bibliothecarius.models.canon import Canon


class Translation(Base):
    __tablename__ = "translations"

    translation_id: Mapped[int] = mapped_column(primary_key=True)
    canon_id: Mapped[int] = mapped_column(
        Integer, ForeignKey("canons.canon_id"), nullable=False
    )
    name: Mapped[str] = mapped_column(String, nullable=False)
    description: Mapped[str] = mapped_column(String, nullable=False)
    abbreviation: Mapped[str] = mapped_column(String, nullable=False)
    language: Mapped[str] = mapped_column(String, nullable=False)
    country: Mapped[str] = mapped_column(String, nullable=False)
    total_verses: Mapped[int] = mapped_column(Integer, nullable=False)
    hash: Mapped[str] = mapped_column(String, nullable=False)

    canon: Mapped["Canon"] = relationship()

    def __repr__(self) -> str:
        return f"{self.name} ({self.language} - {self.canon.name})"
