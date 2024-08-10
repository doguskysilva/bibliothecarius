from click.testing import CliRunner
from dotenv import load_dotenv
from bibliothecarius import entities
from bibliothecarius.main import cli
from bibliothecarius.repository import BookRepository, CanonRepository

load_dotenv()


def test_sync_bible(runner: CliRunner, bibliothecarius_context):
    book_repository = BookRepository(bibliothecarius_context.db_session)
    canon_repository = CanonRepository(bibliothecarius_context.db_session)

    print(book_repository)
    print(canon_repository)
