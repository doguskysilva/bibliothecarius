from bibliothecarius.models.book import Book


def row_to_book(row: dict) -> Book:
    return Book(
        book_id=row["id"],
        testament=row["testament"],
        name=row["name"],
        abbreviation=row["name"].replace("_", "")[:3],
        total_chapters=row["chapters"],
    )
