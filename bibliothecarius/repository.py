from typing import List
from sqlalchemy import func, insert, select
from sqlalchemy.orm import Session
from bibliothecarius import entities
from bibliothecarius.models.book import Book
from bibliothecarius.models.canon import BookCanon, Canon
from bibliothecarius.models.translation import Translation
from bibliothecarius.models.verse import Verse


class BookRepository:
    def __init__(self, session: Session) -> None:
        self.session = session

    def by_id(self, id: int):
        stmt = select(Book).where(Book.book_id == id)
        return self.session.scalar(stmt)

    def all(self):
        return self.session.query(Book).all()

    def add(self, book: entities.Book):
        stmt = insert(Book).returning(Book)
        result = self.session.scalar(stmt, book._asdict())
        self.session.commit()
        return result

    def add_many(self, books: List[entities.Book]):
        stmt = insert(Book)
        self.session.execute(stmt, [book._asdict() for book in books])
        self.session.commit()


class CanonRepository:
    def __init__(self, session: Session) -> None:
        self.session = session

    def all(self):
        return self.session.query(Canon).all()

    def by_name(self, name: str):
        stmt = select(Canon).where(Canon.name == name)
        return self.session.scalar(stmt)

    def add(self, canon: entities.Canon):
        stmt = insert(Canon).returning(Canon)
        result = self.session.scalar(stmt, canon._asdict())
        self.session.commit()
        return result

    def add_many(self, canons: List[entities.Canon]):
        stmt = insert(Canon)
        self.session.execute(stmt, [canon._asdict() for canon in canons])
        self.session.commit()


class BookCanonRespository:
    def __init__(self, session: Session) -> None:
        self.session = session

    def all_by_canon(self, canon: Canon):
        stmt = (
            select(BookCanon)
            .where(BookCanon.canon_id == canon.canon_id)
            .order_by(BookCanon.sort_index)
        )
        return self.session.scalars(stmt).all()


class TranslationRepository:
    def __init__(self, session: Session) -> None:
        self.session = session

    def all(self):
        stmt = select(Translation)
        return self.session.scalars(stmt).all()

    def by_id(self, id: int):
        stmt = select(Translation).where(Translation.translation_id == id)
        return self.session.scalar(stmt)

    def add(self, translation: entities.Translation):
        stmt = insert(Translation).returning(Translation)
        result = self.session.scalar(stmt, translation)
        self.session.commit()
        return result

    def add_many(self, translations: List[entities.Translation]):
        stmt = insert(Translation)
        self.session.execute(
            stmt, [translation._asdict() for translation in translations]
        )
        self.session.commit()


class VerseRepository:
    def __init__(self, session: Session) -> None:
        self.session = session

    def count_by_translation(self, translation: Translation):
        stmt = select(func.count(Verse.verse_id)).where(
            Verse.translation_id == translation.translation_id
        )
        return self.session.scalars(stmt).one()

    def create_verse(self, verse: entities.Verse):
        stmt = insert(Verse).returning(Verse)
        self.session.execute(stmt, verse._asdict())
        self.session.commit()
