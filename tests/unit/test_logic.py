from bibliothecarius.logic import generate_dict_ids
from tests.factories.factory import BookCanonFactory


def test_should_be_generate_empty_dict():
    assert {} == generate_dict_ids([])


def test_generate_dict_books():
    book_canon_1 = BookCanonFactory(bookId=1010, sortIndex=1)
    book_canon_2 = BookCanonFactory(bookId=1020, sortIndex=2)

    expected_output = {
        1: book_canon_1.bookId,
        2: book_canon_2.bookId
    }

    assert expected_output == generate_dict_ids([book_canon_1, book_canon_2])
