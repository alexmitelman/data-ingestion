from sqlmodel import create_engine, Session
from config import settings
from contextlib import contextmanager
import logging


logging.getLogger("sqlalchemy.engine.Engine").setLevel(logging.WARNING)
engine = create_engine(settings.DATABASE_URL, echo=False)

@contextmanager
def get_session():
    session = Session(engine)
    try:
        yield session
    finally:
        session.close()
