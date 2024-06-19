from sqlalchemy.orm import Session
from bibliothecarius.models.book import Book


class BookRepository:
    def __init__(self, session: Session) -> None:
        self.session = session

    def get_all(self):
        return self.session.query(Book).all()

    def create_book(self, book: Book):
        with self.session as session:
            session.add(book)
            session.commit()
