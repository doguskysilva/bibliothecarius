from typing import Dict, List
from bibliothecarius.models.canon import BookCanon


def generate_dict_ids(books_canon: List[BookCanon]) -> Dict[int, int]:
    dict_ids = dict()

    for book_canon in books_canon:
        dict_ids[book_canon.sort_index] = book_canon.book_id

    return dict_ids
