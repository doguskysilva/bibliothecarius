from click.testing import CliRunner
from dotenv import load_dotenv
from bibliothecarius import entities
from bibliothecarius.main import cli
from bibliothecarius.repository import BookRepository, CanonRepository

load_dotenv()


def test_relation_canon_books(runner: CliRunner, bibliothecarius_context):
    book_repository = BookRepository(bibliothecarius_context.db_session)
    canon_repository = CanonRepository(bibliothecarius_context.db_session)

    book = entities.Book(
        book_id=1000,
        name="any-book",
        testament="old",
        abbreviation="anb",
        total_chapters=42,
    )
    canon = entities.Canon(canon_id=2000, name="any-canon", tradition="any", total_books=1)
    book_repository.add_many([book])
    canon_repository.add_many([canon])

    assert len(book_repository.all()) == 1
    assert canon_repository.by_name("any-canon").canon_id == 2000

    with runner.isolated_filesystem():
        with open("books.csv", "w") as file:
            file.write("book_id,sort_index\n1000,1")

        result = runner.invoke(
            cli,
            ["canon-books-sync", "--canon", "any-canon", "--books", "books.csv"],
            obj=bibliothecarius_context
        )
        assert result.exit_code == 0
        assert "Start relation books to any-canon" in result.output

        canon_saved = canon_repository.by_name("any-canon")
        assert len(canon_saved.books) == 1


def test_relation_canon_books_should_be_false(runner: CliRunner, bibliothecarius_context):
    book_repository = BookRepository(bibliothecarius_context.db_session)
    canon_repository = CanonRepository(bibliothecarius_context.db_session)

    book = entities.Book(
        book_id=1001,
        name="any-book",
        testament="old",
        abbreviation="anb",
        total_chapters=42,
    )
    canon = entities.Canon(canon_id=2001, name="any-canon2", tradition="any", total_books=2)
    book_repository.add_many([book])
    canon_repository.add_many([canon])

    with runner.isolated_filesystem():
        with open("books.csv", "w") as file:
            file.write("book_id,sort_index\n1001,1")

        result = runner.invoke(
            cli,
            ["canon-books-sync", "--canon", "any-canon2", "--books", "books.csv"],
            obj=bibliothecarius_context
        )

        assert "Was expected 2 book, but resource has 1" in result.output

        canon_saved = canon_repository.by_name("any-canon2")
        assert len(canon_saved.books) == 0
