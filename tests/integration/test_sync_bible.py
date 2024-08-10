from click.testing import CliRunner
from dotenv import load_dotenv
from bibliothecarius.entities import CanonBook
from bibliothecarius.main import cli
from bibliothecarius.repository import (
    BookCanonRespository,
    BookRepository,
    CanonRepository,
    TranslationRepository,
    VerseRepository,
)
from tests.factories.factory_entities import (
    BookFactoryEntity,
    CanonFactoryEntity,
    TranslationFactoryEntity,
)

load_dotenv()


def test_should_be_sync_all_verses(runner: CliRunner, bibliothecarius_context):
    book_repository = BookRepository(bibliothecarius_context.db_session)
    canon_repository = CanonRepository(bibliothecarius_context.db_session)
    book_canon_repository = BookCanonRespository(bibliothecarius_context.db_session)
    translation_repository = TranslationRepository(bibliothecarius_context.db_session)
    verse_repositoty = VerseRepository(bibliothecarius_context.db_session)

    book = BookFactoryEntity()
    canon = CanonFactoryEntity()
    translation = TranslationFactoryEntity(canon_id=canon.canon_id)
    canon_book = CanonBook(book_id=book.book_id, canon_id=canon.canon_id, sort_index=1)

    created_book = book_repository.add(book)
    created_canon = canon_repository.add(canon)
    created_translation = translation_repository.add(translation)
    book_canon_repository.add(created_canon, created_book, canon_book=canon_book)

    with runner.isolated_filesystem():
        with open("bible.csv", "w") as file:
            file.write(
                "book_id;version_abbreviation;chapter;number;text\n1;any;1;1;Any Text"
            )

        result = runner.invoke(
            cli,
            [
                "sync-bible",
                "--translation",
                created_translation.translation_id,
                "--bible",
                "bible.csv",
            ],
            obj=bibliothecarius_context,
        )

        assert result.exit_code == 0
        assert verse_repositoty.count_by_translation(created_translation) == 1
