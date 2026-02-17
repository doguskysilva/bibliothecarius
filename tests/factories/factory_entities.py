import factory

from bibliothecarius.entities import Book, Canon, Translation


class BookFactoryEntity(factory.Factory):
    class Meta:
        model = Book

    id = factory.Faker("random_int")
    name = factory.Faker("word")
    testament = factory.Faker("random_element", elements=["new", "old"])
    abbreviation = factory.Faker("word")
    totalChapters = factory.Faker("random_int")


class CanonFactoryEntity(factory.Factory):
    class Meta:
        model = Canon

    id = factory.Faker("random_int")
    name = factory.Faker("word")
    tradition = factory.Faker("word")
    totalBooks = factory.Faker("random_digit")


class TranslationFactoryEntity(factory.Factory):
    class Meta:
        model = Translation

    id = factory.Faker("random_int")
    canonId = factory.Faker("random_int")
    name = factory.Faker("word")
    description = factory.Faker("text")
    abbreviation = factory.Faker("word")
    language = factory.Faker("language_code")
    country = factory.Faker("country_code")
    totalVerses = factory.Faker("random_int")
    hash = factory.Faker("sha256")


# class BookCanonFactory(factory.Factory):
#     class Meta:
#         model = BookCanon

#     id = factory.Faker('random_int')
#     canonId = factory.Faker('random_int')
#     bookId = factory.Faker('random_int')
#     sortIndex = factory.Faker('random_int')
#     book = factory.SubFactory(BookFactory)
