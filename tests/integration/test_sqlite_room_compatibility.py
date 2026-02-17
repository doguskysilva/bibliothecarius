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
