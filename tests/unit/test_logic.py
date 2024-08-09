from bibliothecarius.logic import generate_dict_ids
from tests.factories.factory import BookCanonFactory


def test_should_be_generate_empty_dict():
    assert {} == generate_dict_ids([])


def test_generate_dict_books():
    book_canon_1 = BookCanonFactory(book_id=1010, sort_index=1)
    book_canon_2 = BookCanonFactory(book_id=1020, sort_index=2)

    expected_output = {
        1: book_canon_1.book_id,
        2: book_canon_2.book_id
    }

    assert expected_output == generate_dict_ids([book_canon_1, book_canon_2])
