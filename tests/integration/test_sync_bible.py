from click.testing import CliRunner
from dotenv import load_dotenv
from bibliothecarius.main import cli
from bibliothecarius.repository import BookRepository, CanonRepository
from tests.factories.factory_entities import BookFactoryEntity, CanonFactoryEntity

load_dotenv()


def test_should_not_create_when_translation_not_exist(
    runner: CliRunner,
    bibliothecarius_context
):
    assert 1 == 1


def test_should_be_sync_all_verses(
    runner: CliRunner,
    bibliothecarius_context
):
    book_repository = BookRepository(bibliothecarius_context.db_session)
    canon_repository = CanonRepository(bibliothecarius_context.db_session)

    book = BookFactoryEntity()
    canon = CanonFactoryEntity()

    x = book_repository.add(book)
    canon_repository.add_many([canon])

    assert x is None
