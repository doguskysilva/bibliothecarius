from contextlib import contextmanager

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def get_engine(database_url):
    return create_engine(database_url, connect_args={"check_same_thread": False})


def get_session(engine):
    return sessionmaker(autocommit=False, autoflush=False, bind=engine)


@contextmanager
def db_session(database_url):
    engine = get_engine(database_url)
    SessionLocal = get_session(engine)
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()
