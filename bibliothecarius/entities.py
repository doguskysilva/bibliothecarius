import collections

Canon = collections.namedtuple(
    "Canon", ["id", "name", "tradition", "totalBooks"]
)

Book = collections.namedtuple(
    "Book", ["id", "name", "testament", "abbreviation", "totalChapters"]
)

CanonBook = collections.namedtuple("CanonBook", ["canonId", "bookId", "sortIndex"])

Translation = collections.namedtuple(
    "Translation",
    [
        "id",
        "name",
        "description",
        "language",
        "country",
        "abbreviation",
        "totalVerses",
        "canonId",
        "hash",
    ],
)

Verse = collections.namedtuple(
    "Verse", ["bookId", "translationId", "chapter", "verseNumber", "content"]
)
