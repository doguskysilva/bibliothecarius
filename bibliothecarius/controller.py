import csv

import click

from bibliothecarius.logic import generate_dict_ids
from bibliothecarius.models.canon import BookCanon
from bibliothecarius.mappers import (
    row_to_book,
    row_to_canon,
    row_to_canon_book,
    row_to_translation,
    row_to_verse,
)
from sqlalchemy.orm import Session
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

    canon = canon_repository.by_name(canon_name)

    with open(filename, "r") as text_wrapper:
        csv_reader = csv.DictReader(text_wrapper, delimiter=",")
        books_canon = [row_to_canon_book(canon.canon_id, row) for row in csv_reader]

        if canon.total_books == len(books_canon):
            for book_canon in books_canon:
                relation = BookCanon(sort_index=book_canon.sort_index)
                relation.book = book_repository.by_id(book_canon.book_id)
                canon.books.append(relation)
                session.commit()
        else:
            exception = click.ClickException(
                f"Was expected {canon.total_books} book, but resource has {len(books_canon)}"
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


def check_bible_by_tranlation(translation_id, session: Session):
    translation_repository = TranslationRepository(session)
    verse_repository = VerseRepository(session)

    translation = translation_repository.by_id(translation_id)
    total_verses = verse_repository.count_by_translation(translation)

    if total_verses == translation.total_verses:
        click.echo(f"Bible {translation.name} is consistent with {total_verses}")
    else:
        click.echo(f"Bible {translation.name} is not consistent")
        click.echo(f"Expected {translation.total_verses} - {total_verses}")


def sync_bible_to_database(translation_id: int, filename: str, session: Session):
    translation_repository = TranslationRepository(session)
    book_canon_repository = BookCanonRespository(session)
    verse_repository = VerseRepository(session)

    translation = translation_repository.by_id(translation_id)
    books_canon = book_canon_repository.all_by_canon(translation.canon)

    click.echo(f"Loading to translation - {translation.name}")

    dicts_ids = generate_dict_ids(books_canon)

    with open(filename, "r") as text_wrapper:
        csv_reader = csv.DictReader(text_wrapper, delimiter=";")

        for row in csv_reader:
            book_id = int(row["book_id"])
            verse = row_to_verse(
                translation.translation_id,
                dicts_ids[book_id],
                row
            )
            verse_repository.create_verse(verse)

    return 1
