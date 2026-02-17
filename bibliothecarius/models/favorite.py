from bibliothecarius.models.base import Base
from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy import ForeignKey, Integer

from bibliothecarius.models.verse import Verse


class Favorite(Base):
    __tablename__ = "favorites"

    favorite_id: Mapped[int] = mapped_column("id", primary_key=True)
    verse_id: Mapped[int] = mapped_column("verseId", ForeignKey("verses.id"))
    created_at: Mapped[int] = mapped_column("createdAt", Integer, nullable=False)
    updated_at: Mapped[int] = mapped_column("updatedAt", Integer, nullable=False)

    verse: Mapped["Verse"] = relationship()
