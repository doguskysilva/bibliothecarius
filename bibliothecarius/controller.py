import csv

from bibliothecarius.mappers import row_to_book
from sqlalchemy.orm import Session
from bibliothecarius.repository import BookRepository


def sync_file_to_database(filename: str, session: Session):
    book_repository = BookRepository(session)

    with open(filename, "r") as text_wrapper:
        csv_reader = csv.DictReader(text_wrapper, delimiter=";")
        for row in csv_reader:
            book = row_to_book(row)
            book_repository.create_book(book)
