from faker import Faker

from bibliothecarius.mappers import (
    row_to_book,
    row_to_canon,
    row_to_canon_book,
    row_to_translation,
    row_to_verse,
)


def test_row_to_book(faker: Faker):
    row = {
        "id": faker.random_int(),
        "name": "1_book",
        "testament": faker.word(),
        "chapters": faker.random_digit(),
    }
    output = row_to_book(row)

    assert row["id"] == output.book_id
    assert row["name"] == output.name
    assert "1bo" == output.abbreviation
    assert row["testament"] == output.testament
    assert row["chapters"] == output.total_chapters


def test_row_to_canon(faker: Faker):
    row = {
        "id": faker.random_int(),
        "name": faker.word(),
        "tradition": faker.word(),
        "total_books": faker.random_int(),
    }
    output = row_to_canon(row)

    assert row["id"] == output.canon_id
    assert row["name"] == output.name
    assert row["tradition"] == output.tradition
    assert row["total_books"] == output.total_books


def test_row_to_canon_book(faker: Faker):
    canon_id = faker.random_int()
    row = {"book_id": faker.random_int(), "sort_index": faker.random_digit()}
    output = row_to_canon_book(canon_id, row)

    assert output.canon_id == canon_id
    assert output.book_id == row["book_id"]
    assert output.sort_index == row["sort_index"]


def test_row_to_translation(faker: Faker):
    row = {
        "id": faker.random_int(),
        "name": faker.word(),
        "description": faker.text(),
        "language": "pt",
        "country": "br",
        "total_verses": faker.random_int(),
        "canon_id": faker.random_int(),
        "hash": faker.sha256(),
    }
    output = row_to_translation(row)

    assert output.translation_id == row["id"]
    assert output.canon_id == row["canon_id"]
    assert output.name == row["name"]
    assert output.description == row["description"]
    assert output.language == row["language"]
    assert output.country == row["country"]
    assert output.total_verses == row["total_verses"]
    assert output.abbreviation == "pt-br"
    assert output.hash == row["hash"]


def test_row_to_verse(faker: Faker):
    translation_id = faker.random_int()
    row = {
        "book_id": faker.random_int(),
        "chapter": faker.random_int(),
        "number": faker.random_int(),
        "text": faker.text(),
    }
    output = row_to_verse(translation_id, row)

    assert translation_id == output.translation_id
    assert row["book_id"] == output.book_id
    assert row["chapter"] == output.chapter
    assert row["number"] == output.verse_number
    assert row["text"] == output.content
