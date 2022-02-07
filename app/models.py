from contextlib import contextmanager

from flask_login import UserMixin
from sqlalchemy import Column, Integer, String, create_engine, ForeignKey, TEXT, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker, relationship

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


class User(UserMixin, Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(200), unique=True, nullable=False)
    password = Column(String(200), nullable=False)

    def __init__(self, username, password):
        self.username = username
        self.password = password


@login_manager.user_loader
def load_user(user_id):
    with session() as s:
        user = s.query(User).get(int(user_id))
    return user


# def load_user(user_id):
# with session() as s:
    #     user_id = s.query(User).get_id(user_id)
    #     print(user_id)
    # return user_id


class Category(Base):
    __tablename__ = 'categories'
    id = Column(Integer, primary_key=True)
    avatar = Column(String(200), unique=True)
    name = Column(String(200), unique=True, nullable=False)
    description = Column(String(200), nullable=False)
    product_info = relationship("Product", backref="category", lazy='dynamic', cascade="all, delete, delete-orphan")


class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True)
    category_id = Column(Integer, ForeignKey('categories.id'), nullable=False)
    product_photo = relationship("Photo", backref="product", lazy='dynamic', cascade="all, delete, delete-orphan")
    name = Column(String(200), unique=True, nullable=False)
    description = Column(TEXT, nullable=False)
    price = Column(Integer, nullable=False)
    available = Column(Boolean, default=False)


class Photo(Base):
    __tablename__ = 'photos'
    id = Column(Integer, primary_key=True)
    product_id = Column(Integer, ForeignKey('products.id'), nullable=False)
    photo = Column(String(200), unique=True)




