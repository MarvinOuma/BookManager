from lib.main import session, Author, Genre, Book, Publisher

# Clear existing data to avoid unique constraint errors
session.query(Book).delete()
session.query(Author).delete()
session.query(Genre).delete()
session.query(Publisher).delete()
session.commit()

# Existing authors, genres, and publishers
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

p1 = Publisher(name="Bloomsbury")
p2 = Publisher(name="Secker & Warburg")
p3 = Publisher(name="Allen & Unwin")
p4 = Publisher(name="Collins Crime Club")
p5 = Publisher(name="Doubleday")

# Books with publication year and publisher
b1 = Book(title="Harry Potter", author=a1, genre=g1, publication_year=1997, publisher=p1)
b2 = Book(title="1984", author=a2, genre=g2, publication_year=1949, publisher=p2)
b3 = Book(title="The Hobbit", author=a3, genre=g1, publication_year=1937, publisher=p3)
b4 = Book(title="Murder on the Orient Express", author=a4, genre=g3, publication_year=1934, publisher=p4)
b5 = Book(title="The Shining", author=a5, genre=g4, publication_year=1977, publisher=p5)
b6 = Book(title="The Lord of the Rings", author=a3, genre=g1, publication_year=1954, publisher=p3)
b7 = Book(title="Carrie", author=a5, genre=g4, publication_year=1974, publisher=p5)
b8 = Book(title="Animal Farm", author=a2, genre=g2, publication_year=1945, publisher=p2)
b9 = Book(title="And Then There Were None", author=a4, genre=g3, publication_year=1939, publisher=p4)
b10 = Book(title="It", author=a5, genre=g4, publication_year=1986, publisher=p5)

session.add_all([a1, a2, a3, a4, a5, g1, g2, g3, g4, g5, p1, p2, p3, p4, p5,
                 b1, b2, b3, b4, b5, b6, b7, b8, b9, b10])
session.commit()
