from click.testing import CliRunner
from dotenv import load_dotenv
from bibliothecarius.main import cli
from bibliothecarius.models.book import Book
from bibliothecarius.models.canon import Canon
from bibliothecarius.repository import BookRepository, CanonRepository

load_dotenv()


def test_relation_canon_books(runner: CliRunner, bibliothecarius_context):
    book_repository = BookRepository(bibliothecarius_context.db_session)
    canon_repository = CanonRepository(bibliothecarius_context.db_session)

    book = Book(
        book_id=1001,
        name="any-book",
        testament="old",
        abbreviation="anb",
        total_chapters=42,
    )
    canon = Canon(canon_id=2001, name="any-canon", tradition="any", total_books=1)
    book_repository.create_book(book)
    canon_repository.create_canons([canon])

    assert len(book_repository.get_all()) == 1
    assert len(canon_repository.get_all()) == 1

    with runner.isolated_filesystem():
        with open("books.csv", "w") as file:
            file.write("book_id;sort_index\n1001;1")

        result = runner.invoke(
            cli,
            ["relation-canon-books", "--canon", "any-canon", "--books", "books.csv"],
            obj=bibliothecarius_context
        )
        assert result.exit_code == 0
        assert "Start relation books to any-canon" in result.output

        # assert len(book_repository.get_all()) == 1
