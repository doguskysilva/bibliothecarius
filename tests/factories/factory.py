import factory

from bibliothecarius.models.book import Book
from bibliothecarius.models.canon import BookCanon


class BookFactory(factory.Factory):
    class Meta:
        model = Book

    book_id = factory.Faker('random_int')
    testament = factory.Faker('random_element', elements=['new', 'old'])
    name = factory.Faker('name')
    abbreviation = factory.Faker('random_letters', length=3)
    total_chapters = factory.Faker('random_int')


class BookCanonFactory(factory.Factory):
    class Meta:
        model = BookCanon

    book_canon_id = factory.Faker('random_int')
    canon_id = factory.Faker('random_int')
    book_id = factory.Faker('random_int')
    sort_index = factory.Faker('random_int')
    book = factory.SubFactory(BookFactory)
