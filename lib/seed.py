from lib.main import session, Author, Genre, Book

# Clear existing data to avoid unique constraint errors
session.query(Book).delete()
session.query(Author).delete()
session.query(Genre).delete()
session.commit()

# Existing authors and genres
a1 = Author(name="J.K. Rowling")
a2 = Author(name="George Orwell")
a3 = Author(name="J.R.R. Tolkien")
a4 = Author(name="Agatha Christie")
a5 = Author(name="Stephen King")

g1 = Genre(name="Fantasy")
g2 = Genre(name="Dystopian")
g3 = Genre(name="Mystery")
g4 = Genre(name="Horror")
g5 = Genre(name="Science Fiction")

# Books
b1 = Book(title="Harry Potter", author=a1, genre=g1)
b2 = Book(title="1984", author=a2, genre=g2)
b3 = Book(title="The Hobbit", author=a3, genre=g1)
b4 = Book(title="Murder on the Orient Express", author=a4, genre=g3)
b5 = Book(title="The Shining", author=a5, genre=g4)
b6 = Book(title="The Lord of the Rings", author=a3, genre=g1)
b7 = Book(title="Carrie", author=a5, genre=g4)
b8 = Book(title="Animal Farm", author=a2, genre=g2)
b9 = Book(title="And Then There Were None", author=a4, genre=g3)
b10 = Book(title="It", author=a5, genre=g4)

session.add_all([a1, a2, a3, a4, a5, g1, g2, g3, g4, g5,
                 b1, b2, b3, b4, b5, b6, b7, b8, b9, b10])
session.commit()
