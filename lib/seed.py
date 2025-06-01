from lib.main import session, Author, Genre, Book

a1 = Author(name="J.K. Rowling")
a2 = Author(name="George Orwell")
g1 = Genre(name="Fantasy")
g2 = Genre(name="Dystopian")

b1 = Book(title="Harry Potter", author=a1, genre=g1)
b2 = Book(title="1984", author=a2, genre=g2)

session.add_all([a1, a2, g1, g2, b1, b2])
session.commit()
