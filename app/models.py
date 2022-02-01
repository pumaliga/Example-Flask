from contextlib import contextmanager

from flask_login import UserMixin
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker

from . import login_manager


Base = declarative_base()

host = "localhost"
engine = create_engine(f'postgresql://flask_user:12345@{host}:5433/flask')


@contextmanager
def session():
    connection = engine.connect()
    db_session = scoped_session(sessionmaker(autocommit=False, autoflush=True, bind=engine))
    try:
        yield db_session
    except Exception as e:
        print(e)
    finally:
        db_session.remove()
        connection.close()


class User(UserMixin,Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(200), unique=True, nullable=False)
    password = Column(String(200), nullable=False)

    def __init__(self, username, password):
        self.username = username
        self.password = password


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))