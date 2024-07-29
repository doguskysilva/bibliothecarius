from bibliothecarius.mappers import row_to_book, row_to_canon


def test_row_to_book():
    row = {
        "id": 42,
        "name": "1_book",
        "testament": "old",
        "chapters": 1,
    }
    output = row_to_book(row)

    assert row["id"] == output.book_id
    assert row["name"] == output.name
    assert "1bo" == output.abbreviation
    assert row["testament"] == output.testament
    assert row["chapters"] == output.total_chapters


def test_row_to_canon():
    row = {
        "id": 42,
        "name": "any_canon",
        "tradition": "any_tradition",
        "total_books": 42
    }
    output = row_to_canon(row)
 
    assert row["id"] == output.canon_id
    assert row["name"] == output.name
    assert row["tradition"] == output.tradition
    assert row["total_books"] == output.total_books
