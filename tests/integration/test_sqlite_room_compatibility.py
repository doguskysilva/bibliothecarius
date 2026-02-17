from sqlalchemy import text


def test_should_create_room_compatible_indexes(db):
    verses_indexes = {
        index[1] for index in db.execute(text("PRAGMA index_list('verses')")).fetchall()
    }
    assert "ix_verses_book_id" in verses_indexes
    assert "ix_verses_translation_id" in verses_indexes
    assert "ix_verses_translation_id_book_id_chapter_verse_number" in verses_indexes

    translations_indexes = {
        index[1]
        for index in db.execute(text("PRAGMA index_list('translations')")).fetchall()
    }
    assert "ix_translations_canon_id" in translations_indexes


def test_should_use_room_friendly_column_names(db):
    table_columns = {
        table_name: {
            column[1]
            for column in db.execute(text(f"PRAGMA table_info('{table_name}')")).fetchall()
        }
        for table_name in [
            "books",
            "canons",
            "translations",
            "verses",
            "book_canon",
        ]
    }

    assert "id" in table_columns["books"]
    assert "totalChapters" in table_columns["books"]
    assert "id" in table_columns["canons"]
    assert "totalBooks" in table_columns["canons"]
    assert "id" in table_columns["translations"]
    assert "canonId" in table_columns["translations"]
    assert "totalVerses" in table_columns["translations"]
    assert "id" in table_columns["verses"]
    assert "translationId" in table_columns["verses"]
    assert "bookId" in table_columns["verses"]
    assert "verseNumber" in table_columns["verses"]
    assert "saidJesus" in table_columns["verses"]
    assert "id" in table_columns["book_canon"]
    assert "canonId" in table_columns["book_canon"]
    assert "bookId" in table_columns["book_canon"]
    assert "sortIndex" in table_columns["book_canon"]
