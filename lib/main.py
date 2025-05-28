from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, declarative_base, sessionmaker

Base = declarative_base()
engine = create_engine('sqlite:///lib/book.db')
Session = sessionmaker(bind=engine)
session = Session()

class Author(Base):
    __tablename__ = 'authors'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    books = relationship('Book', back_populates='author')

class Genre(Base):
    __tablename__ = 'genres'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    books = relationship('Book', back_populates='genre')

class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    author_id = Column(Integer, ForeignKey('authors.id'))
    genre_id = Column(Integer, ForeignKey('genres.id'))
    author = relationship('Author', back_populates='books')
    genre = relationship('Genre', back_populates='books')
