import click
import os
from dotenv import load_dotenv

from bibliothecarius.controller import (
    get_canon_by_name,
    mount_canon,
    sync_books_to_database,
    sync_canons_to_database,
    sync_translations_to_database,
)
from bibliothecarius.context import db_session


class BibliothecariusContext:
    def __init__(self) -> None:
        self.db_session = None


@click.group()
@click.pass_context
def cli(ctx):
    load_dotenv()
    ctx.ensure_object(BibliothecariusContext)
    if ctx.obj.db_session is None:
        with db_session(os.environ.get("DATABASE_URL", "")) as session:
            ctx.obj.db_session = session
            ctx.call_on_close(session.close)


@cli.command()
def hello():
    click.echo("Hello bibliothecarius!")


@cli.command()
@click.argument("filename", type=click.Path(exists=True))
@click.pass_context
def sync_books(ctx, filename):
    click.echo("Start sync books")
    sync_books_to_database(filename, ctx.obj.db_session)


@cli.command()
@click.argument("filename", type=click.Path(exists=True))
@click.pass_context
def sync_canons(ctx, filename):
    click.echo("Start sync canons")
    sync_canons_to_database(filename, ctx.obj.db_session)


@cli.command()
@click.option("-c", "--canon", type=str)
@click.option("-b", "--books", type=click.Path(exists=True))
@click.pass_context
def relation_canon_books(ctx, canon, books):
    click.echo(f"Start relation books to {canon}")
    mount_canon(canon, books, ctx.obj.db_session)


@cli.command()
@click.option("-c", "--canon", "canon_name",
              type=click.Choice(['roman_catholics', 'protestant'],
                                case_sensitive=False))
@click.pass_context
def list_books(ctx, canon_name):
    canon = get_canon_by_name(canon_name, ctx.obj.db_session)
    for relation in canon.books:
        click.echo(f"{relation.sort_index} - {relation.book.name}")


@cli.command()
@click.argument("filename", type=click.Path(exists=True))
@click.pass_context
def sync_translations(ctx, filename):
    click.echo("Start sync translations")
    sync_translations_to_database(filename, ctx.obj.db_session)


def main():
    cli(obj={})


if __name__ == "__main__":
    main()
