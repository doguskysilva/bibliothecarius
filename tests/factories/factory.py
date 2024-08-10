import factory

from bibliothecarius.models.book import Book
from bibliothecarius.models.canon import BookCanon, Canon
from bibliothecarius.models.translation import Translation


class BookFactory(factory.Factory):
    class Meta:
        model = Book

    book_id = factory.Faker('random_int')
    testament = factory.Faker('random_element', elements=['new', 'old'])
    name = factory.Faker('name')
    abbreviation = factory.Faker('random_letters', length=3)
    total_chapters = factory.Faker('random_int')


class CanonFactory(factory.Factory):
    class Meta:
        model = Canon

    canon_id = factory.Faker('random_int')
    tradition = factory.Faker('name')
    name = factory.Faker('name')
    description = factory.Faker('text')
    total_book = factory.Faker('random_digit')


class BookCanonFactory(factory.Factory):
    class Meta:
        model = BookCanon

    book_canon_id = factory.Faker('random_int')
    canon_id = factory.Faker('random_int')
    book_id = factory.Faker('random_int')
    sort_index = factory.Faker('random_int')
    book = factory.SubFactory(BookFactory)


class TranslationFactory(factory.Factory):
    class Meta:
        model = Translation

    translation_id = factory.Faker('random_int')
    canon_id = factory.Faker('random_int')
    name = factory.Faker('word')
    description = factory.Faker('text')
    abbreviation = factory.Faker('word')
    language = factory.Faker('language_code')
    country = factory.Faker('country_code')
    total_verses = factory.Faker('random_int')
    canon = factory.SubFactory(CanonFactory)
