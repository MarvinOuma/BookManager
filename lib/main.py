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

class Publisher(Base):
    __tablename__ = 'publishers'
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    books = relationship('Book', back_populates='publisher')

class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    publication_year = Column(Integer, nullable=True)
    author_id = Column(Integer, ForeignKey('authors.id'))
    genre_id = Column(Integer, ForeignKey('genres.id'))
    publisher_id = Column(Integer, ForeignKey('publishers.id'), nullable=True)
    author = relationship('Author', back_populates='books')
    genre = relationship('Genre', back_populates='books')
    publisher = relationship('Publisher', back_populates='books')
