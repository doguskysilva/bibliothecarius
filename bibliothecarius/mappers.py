from bibliothecarius import entities


def row_to_book(row: dict) -> entities.Book:
    return entities.Book(
        book_id=row["id"],
        name=row["name"],
        testament=row["testament"],
        abbreviation=row["name"].replace("_", "")[:3],
        total_chapters=row["chapters"],
    )


def row_to_canon(row: dict) -> entities.Canon:
    return entities.Canon(
        canon_id=row["id"],
        name=row["name"],
        tradition=row["tradition"],
        total_books=row["total_books"]
    )


def row_to_translation(row: dict) -> entities.Translation:
    return entities.Translation(
        translation_id=row["id"],
        name=row["name"],
        description=row["description"],
        abbreviation=f"{row["language"]}-{row["country"]}".lower(),
        language=row["language"],
        country=row["country"],
        total_verses=row["total_verses"],
        canon_id=row["canon_id"]
    )


def row_to_canon_book(canon_id: int, row: dict) -> entities.CanonBook:
    return entities.CanonBook(
        canon_id=canon_id,
        book_id=row["book_id"],
        sort_index=row["sort_index"]
    )


def row_to_verse(translation_id: int, row: dict) -> entities.Verse:
    return entities.Verse(
        translation_id=translation_id,
        book_id=row["book_id"],
        chapter=row["chapter"],
        verse_number=row["number"],
        content=row["text"]
    )
