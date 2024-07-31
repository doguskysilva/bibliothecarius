import collections

Canon = collections.namedtuple('Canon', ['canon_id', 'name', 'tradition', 'total_books'])
Book = collections.namedtuple('Book', ['book_id', 'name', 'abbreviation' 'total_chapters', 'testament'])
CanonBook = collections.namedtuple('CanonBook', ['canon_id', 'book_id', 'sort_index'])
