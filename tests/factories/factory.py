import factory

from bibliothecarius.models.book import Book
from bibliothecarius.models.canon import BookCanon


class BookFactory(factory.Factory):
    class Meta:
        model = Book

    id = factory.Faker('random_int')
    testament = factory.Faker('random_element', elements=['new', 'old'])
    name = factory.Faker('name')
    abbreviation = factory.Faker('random_letters', length=3)
    totalChapters = factory.Faker('random_int')


class BookCanonFactory(factory.Factory):
    class Meta:
        model = BookCanon

    id = factory.Faker('random_int')
    canonId = factory.Faker('random_int')
    bookId = factory.Faker('random_int')
    sortIndex = factory.Faker('random_int')
    book = factory.SubFactory(BookFactory)
