import collections

Canon = collections.namedtuple(
    "Canon", ["canon_id", "name", "tradition", "total_books"]
)

Book = collections.namedtuple(
    "Book", ["book_id", "name", "testament", "abbreviation", "total_chapters"]
)

CanonBook = collections.namedtuple(
    "CanonBook",
    ["canon_id", "book_id", "sort_index"]
)

Translation = collections.namedtuple(
    "Translation",
    [
        "translation_id",
        "name",
        "description",
        "language",
        "country",
        "abbreviation",
        "total_verses",
        "canon_id",
    ],
)

Verse = collections.namedtuple(
    "Verse",
    [
        "book_id",
        "translation_id",
        "chapter",
        "verse_number",
        "content"
    ]
)
