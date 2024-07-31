from bibliothecarius import entities
from bibliothecarius.models.book import Book
from bibliothecarius.models.canon import Canon
from bibliothecarius.models.translation import Translation


def row_to_book(row: dict) -> Book:
    return Book(
        book_id=row["id"],
        testament=row["testament"],
        name=row["name"],
        abbreviation=row["name"].replace("_", "")[:3],
        total_chapters=row["chapters"],
    )


def row_to_canon(row: dict) -> Canon:
    return Canon(
        canon_id=row["id"],
        name=row["name"],
        tradition=row["tradition"],
        total_books=row["total_books"]
    )


def row_to_translation(row: dict) -> Translation:
    return Translation(
        translation_id=row["id"],
        name=row["name"],
        description=row["description"],
        abbreviation=f"{row["language"]}-{row["country"]}".lower(),
        language=row["language"],
        country=row["country"],
        total_books=row["total_books"],
        total_verses=row["total_verses"]
    )


def row_to_canon_book(canon_id: int, row: dict) -> entities.CanonBook:
    return entities.CanonBook(
        canon_id=canon_id,
        book_id=row["book_id"],
        sort_index=row["sort_index"]
    )
