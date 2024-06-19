import pytest

from bibliothecarius.context import db_session, get_engine
from bibliothecarius.models.base import Base
from click.testing import CliRunner
from bibliothecarius.main import BibliothecariusContext


@pytest.fixture(scope="module")
def db():
    database_url = "sqlite:///database/scripturas-test.sqlite"
    engine = get_engine(database_url)
    Base.metadata.create_all(bind=engine)
    with db_session(database_url) as session:
        yield session
    Base.metadata.drop_all(bind=engine)


@pytest.fixture
def runner(db):
    return CliRunner()


@pytest.fixture
def bibliothecarius_context(db):
    ctx = BibliothecariusContext()
    ctx.db_session = db
    return ctx


def setup_modeule(module):
    database_url = "sqlite:///database/scripturas-test.sqlite"
    engine = get_engine(database_url)

    Base.metadata.create_all(bind=engine)
