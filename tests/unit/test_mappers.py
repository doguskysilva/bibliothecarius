from bibliothecarius.mappers import row_to_book


def test_row_to_book():
    row = {
        "id": 42,
        "name": "Any",
        "testament": "old",
        "abbreviation": "any",
        "chapters": 1,
    }
    output = row_to_book(row)

    assert row["id"] == output.book_id
    assert row["name"] == output.name
    assert row["abbreviation"] == output.abbreviation
    assert row["testament"] == output.testament
    assert row["chapters"] == output.total_chapters
