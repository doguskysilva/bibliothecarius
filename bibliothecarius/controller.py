import csv

import click
from sqlalchemy.orm import Session

from bibliothecarius.mappers import (
    row_to_book,
    row_to_canon,
    row_to_canon_book,
    row_to_translation,
    row_to_verse,
)
from bibliothecarius.models.canon import BookCanon
from bibliothecarius.repository import (
    BookCanonRespository,
    BookRepository,
    CanonRepository,
    TranslationRepository,
    VerseRepository,
)


def sync_books_to_database(filename: str, session: Session):
    book_repository = BookRepository(session)

    with open(filename, "r") as text_wrapper:
        csv_reader = csv.DictReader(text_wrapper, delimiter=",")
        books = [row_to_book(book) for book in csv_reader]
        book_repository.add_many(books)


def sync_canons_to_database(filename: str, session: Session):
    canon_repository = CanonRepository(session)

    with open(filename, "r") as text_wrapper:
        csv_reader = csv.DictReader(text_wrapper, delimiter=",")
        canons = [row_to_canon(row) for row in csv_reader]
        canon_repository.add_many(canons)


def sync_translations_to_database(filename: str, session: Session):
    translation_repository = TranslationRepository(session)

    with open(filename, "r") as text_wrapper:
        csv_reader = csv.DictReader(text_wrapper, delimiter=",")
        translations = [row_to_translation(row) for row in csv_reader]
        translation_repository.add_many(translations)


def mount_canon(canon_name: str, filename: str, session: Session):
    canon_repository = CanonRepository(session)
    book_repository = BookRepository(session)
    book_canon_repository = BookCanonRespository(session)

    canon = canon_repository.by_name(canon_name)

    if canon is None:
        exception = click.ClickException("Canon not found")
        exception.show()
        return -1

    with open(filename, "r") as text_wrapper:
        csv_reader = csv.DictReader(text_wrapper, delimiter=",")
        books_canon = [row_to_canon_book(canon.id, row) for row in csv_reader]

        if canon.totalBooks == len(books_canon):
            for book_canon in books_canon:
                book = book_repository.by_id(book_canon.bookId)
                if book is None:
                    exception = click.ClickException(
                        f"Book not found for canon {canon.name}: id={book_canon.bookId}, sortIndex={book_canon.sortIndex}"
                    )
                    exception.show()
                    return -1
                book_canon_repository.add(canon=canon, book=book, canon_book=book_canon)
        else:
            exception = click.ClickException(
                f"Was expected {canon.totalBooks} book, but resource has {len(books_canon)}"
            )
            exception.show()


def get_all_canons(session: Session):
    canon_repository = CanonRepository(session)
    return canon_repository.all()


def get_all_translations(session: Session):
    translation_repository = TranslationRepository(session)
    return translation_repository.all()


def get_translation_by_id(id: int, session: Session):
    translation_repository = TranslationRepository(session)
    return translation_repository.by_id(id)


def get_canon_by_name(canon_name: str, session: Session):
    canon_repository = CanonRepository(session)
    return canon_repository.by_name(canon_name)


def check_bible_by_tranlation(translationId, session: Session):
    translation_repository = TranslationRepository(session)
    verse_repository = VerseRepository(session)

    translation = translation_repository.by_id(translationId)
    totalVerses = verse_repository.count_by_translation(translation)

    if totalVerses == translation.totalVerses:
        click.echo(f"Bible {translation.name} is consistent with {totalVerses}")
    else:
        click.echo(f"Bible {translation.name} is not consistent")
        click.echo(f"Expected {translation.totalVerses} - {totalVerses}")


def sync_bible_to_database(translationId: int, filename: str, session: Session):
    translation_repository = TranslationRepository(session)
    verse_repository = VerseRepository(session)

    translation = translation_repository.by_id(translationId)

    click.echo(f"Loading to translation - {translation.name}")

    with open(filename, "r") as text_wrapper:
        csv_reader = csv.DictReader(text_wrapper, delimiter=";")

        for row in csv_reader:
            verse = row_to_verse(translation.id, row)
            verse_repository.create_verse(verse)

    return 1
