from click.testing import CliRunner
from dotenv import load_dotenv
from bibliothecarius.main import cli
from bibliothecarius.repository import BookRepository

load_dotenv()


def test_books_sync(runner: CliRunner, bibliothecarius_context):
    book_repository = BookRepository(bibliothecarius_context.db_session)

    assert len(book_repository.all()) == 0

    with runner.isolated_filesystem():
        with open("books.csv", "w") as file:
            file.write(
                "id,name,testament,chapters\n1001,Genesis,old,50"
            )

        result = runner.invoke(
            cli, ["books-sync", "books.csv"], obj=bibliothecarius_context
        )
        assert result.exit_code == 0
        assert "Start sync books" in result.output

        assert len(book_repository.all()) == 1
