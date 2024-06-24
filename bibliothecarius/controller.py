import csv

from bibliothecarius.mappers import row_to_book, row_to_translation
from sqlalchemy.orm import Session
from bibliothecarius.repository import BookRepository, TranslationRepository


def sync_books_to_database(filename: str, session: Session):
    book_repository = BookRepository(session)

    with open(filename, "r") as text_wrapper:
        csv_reader = csv.DictReader(text_wrapper, delimiter=";")
        for row in csv_reader:
            book = row_to_book(row)
            book_repository.create_book(book)


def sync_translations_to_database(filename: str, session: Session):
    translation_repository = TranslationRepository(session)

    with open(filename, "r") as text_wrapper:
        csv_reader = csv.DictReader(text_wrapper, delimiter=";")
        translations = [row_to_translation(row) for row in csv_reader]
        translation_repository.create_translations(translations)
