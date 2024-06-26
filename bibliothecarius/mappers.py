from bibliothecarius.models.book import Book
from bibliothecarius.models.translation import Translation


def row_to_book(row: dict) -> Book:
    return Book(
        book_id=row["id"],
        testament=row["testament"],
        name=row["name"],
        abbreviation=row["name"].replace("_", "")[:3],
        total_chapters=row["chapters"],
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
