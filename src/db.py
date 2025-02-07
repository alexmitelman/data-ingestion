import logging
from contextlib import contextmanager

from sqlmodel import Session, create_engine

from config import settings

logging.getLogger("sqlalchemy.engine.Engine").setLevel(logging.WARNING)
engine = create_engine(settings.DATABASE_URL, echo=False)


@contextmanager
def get_session():
    session = Session(engine)
    try:
        yield session
    finally:
        session.close()
