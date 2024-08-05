from typing import List
from sqlalchemy import insert, select
from sqlalchemy.orm import Session
from bibliothecarius import entities
from bibliothecarius.models.book import Book
from bibliothecarius.models.canon import Canon
from bibliothecarius.models.translation import Translation


class BookRepository:
    def __init__(self, session: Session) -> None:
        self.session = session

    def get_by_id(self, id: int):
        stmt = select(Book).where(Book.book_id == id)
        return self.session.scalars(stmt).first()

    def get_all(self):
        return self.session.query(Book).all()

    def create_books(self, books: List[entities.Book]):
        stmt = insert(Book).returning(Book)
        self.session.scalars(stmt, [book._asdict() for book in books])
        self.session.commit()


class CanonRepository:
    def __init__(self, session: Session) -> None:
        self.session = session

    def get_all(self):
        return self.session.query(Canon).all()

    def get_by_name(self, name: str):
        stmt = select(Canon).where(Canon.name == name)
        return self.session.scalars(stmt).first()

    def create_canons(self, canons: List[entities.Canon]):
        stmt = insert(Canon).returning(Canon)
        self.session.scalars(stmt, [canon._asdict() for canon in canons])
        self.session.commit()


class TranslationRepository:
    def __init__(self, session: Session) -> None:
        self.session = session

    def get_all(self):
        stmt = select(Translation)
        return self.session.scalars(stmt).all()

    def create_translations(self, translations: List[entities.Translation]):
        stmt = insert(Translation).returning(Translation)
        self.session.scalars(
            stmt, [translation._asdict() for translation in translations]
        )
        self.session.commit()
