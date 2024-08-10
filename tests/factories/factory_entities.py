import factory

from bibliothecarius.entities import Book, Canon, Translation


class BookFactoryEntity(factory.Factory):
    class Meta:
        model = Book

    book_id = factory.Faker("random_int")
    name = factory.Faker("word")
    testament = factory.Faker("random_element", elements=["new", "old"])
    abbreviation = factory.Faker("word")
    total_chapters = factory.Faker("random_int")


class CanonFactoryEntity(factory.Factory):
    class Meta:
        model = Canon

    canon_id = factory.Faker('random_int')
    name = factory.Faker('word')
    tradition = factory.Faker('word')
    total_books = factory.Faker('random_digit')


class TranslationFactoryEntity(factory.Factory):
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

# class BookCanonFactory(factory.Factory):
#     class Meta:
#         model = BookCanon

#     book_canon_id = factory.Faker('random_int')
#     canon_id = factory.Faker('random_int')
#     book_id = factory.Faker('random_int')
#     sort_index = factory.Faker('random_int')
#     book = factory.SubFactory(BookFactory)
