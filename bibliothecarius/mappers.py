from bibliothecarius import entities


def row_to_book(row: dict) -> entities.Book:
    return entities.Book(
        id=row["id"],
        name=row["name"],
        testament=row["testament"],
        abbreviation=row["name"].replace("_", "")[:3],
        totalChapters=row["chapters"],
    )


def row_to_canon(row: dict) -> entities.Canon:
    return entities.Canon(
        id=row["id"],
        name=row["name"],
        tradition=row["tradition"],
        totalBooks=row["total_books"],
    )


def row_to_translation(row: dict) -> entities.Translation:
    return entities.Translation(
        id=row["id"],
        name=row["name"],
        description=row["description"],
        abbreviation=f"{row['language']}-{row['country']}".lower(),
        language=row["language"],
        country=row["country"],
        totalVerses=row["total_verses"],
        canonId=row["canon_id"],
        hash=row["hash"],
    )


def row_to_canon_book(canonId: int, row: dict) -> entities.CanonBook:
    return entities.CanonBook(
        canonId=canonId, bookId=row["book_id"], sortIndex=row["sort_index"]
    )


def row_to_verse(translationId: int, row: dict) -> entities.Verse:
    return entities.Verse(
        translationId=translationId,
        bookId=int(row["book_id"]),
        chapter=int(row["chapter"]),
        verseNumber=int(row["number"]),
        content=row["text"],
    )
