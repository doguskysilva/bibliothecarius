from typing import List
from sqlalchemy.orm import Session
from bibliothecarius.models.book import Book
from bibliothecarius.models.canon import Canon
from bibliothecarius.models.translation import Translation


class BookRepository:
    def __init__(self, session: Session) -> None:
        self.session = session

    def get_all(self):
        return self.session.query(Book).all()

    def create_book(self, book: Book):
        with self.session as session:
            session.add(book)
            session.commit()


class CanonRepository:
    def __init__(self, session: Session) -> None:
        self.session = session

    def get_all(self):
        return self.session.query(Canon).all()

    def create_canons(self, canons: List[Canon]):
        with self.session as session:
            session.add_all(canons)
            session.commit()


class TranslationRepository:
    def __init__(self, session: Session) -> None:
        self.session = session

    def get_all(self):
        return self.session.query(Translation).all()

    def create_translations(self, translations: List[Translation]):
        with self.session as session:
            session.add_all(translations)
            session.commit()
