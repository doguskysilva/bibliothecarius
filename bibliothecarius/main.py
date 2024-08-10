import click
import os
from dotenv import load_dotenv

from bibliothecarius.controller import (
    check_bible_by_tranlation,
    get_all_translations,
    get_canon_by_name,
    mount_canon,
    sync_bible_to_database,
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
def books_sync(ctx, filename):
    click.echo("Start sync books")
    sync_books_to_database(filename, ctx.obj.db_session)


@cli.command()
@click.argument("filename", type=click.Path(exists=True))
@click.pass_context
def canons_sync(ctx, filename):
    click.echo("Start sync canons")
    sync_canons_to_database(filename, ctx.obj.db_session)


@cli.command()
@click.option("-c", "--canon", type=str)
@click.option("-b", "--books", type=click.Path(exists=True))
@click.pass_context
def canon_books_sync(ctx, canon, books):
    click.echo(f"Start relation books to {canon}")
    mount_canon(canon, books, ctx.obj.db_session)


@cli.command()
@click.option("-c", "--canon", "canon_name",
              type=click.Choice(['roman_catholics', 'protestant'],
                                case_sensitive=False))
@click.pass_context
def books_list(ctx, canon_name):
    canon = get_canon_by_name(canon_name, ctx.obj.db_session)
    for relation in canon.books:
        click.echo(f"{relation.sort_index} - {relation.book.name}")


@cli.command()
@click.pass_context
def translations_list(ctx):
    translations = get_all_translations(ctx.obj.db_session)
    for translation in translations:
        click.echo(f"{translation.translation_id} - {translation.name}")


@cli.command()
@click.argument("filename", type=click.Path(exists=True))
@click.pass_context
def translations_sync(ctx, filename):
    click.echo("Start sync translations")
    sync_translations_to_database(filename, ctx.obj.db_session)


@cli.command()
@click.option("-t", "--translation", "translation_id", type=int)
@click.option("-b", "--bible", "bible", type=click.Path(exists=True))
@click.pass_context
def bible_sync(ctx, translation_id, bible):
    sync_bible_to_database(translation_id, bible, ctx.obj.db_session)


@cli.command()
@click.option("-t", "--translation", "translation_id", type=int)
@click.pass_context
def bible_check(ctx, translation_id):
    check_bible_by_tranlation(translation_id, ctx.obj.db_session)


def main():
    cli(obj={})


if __name__ == "__main__":
    main()
