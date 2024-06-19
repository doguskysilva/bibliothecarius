import click
import os
from dotenv import load_dotenv

from bibliothecarius.controller import sync_file_to_database
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
    sync_file_to_database(filename, ctx.obj.db_session)


def main():
    cli(obj={})


if __name__ == "__main__":
    main()
