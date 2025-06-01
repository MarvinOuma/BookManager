import click
from lib.main import session, Author, Genre, Book

@click.group()
def cli():
    pass

@cli.command()
@click.argument("title")
@click.argument("author_name")
@click.argument("genre_name")
def add(title, author_name, genre_name):
    author = session.query(Author).filter_by(name=author_name).first()
    if not author:
        author = Author(name=author_name)
    genre = session.query(Genre).filter_by(name=genre_name).first()
    if not genre:
        genre = Genre(name=genre_name)
    book = Book(title=title, author=author, genre=genre)
    session.add(book)
    session.commit()
    click.echo(f"Added book: {title}")

@cli.command()
def list():
    books = session.query(Book).all()
    for book in books:
        print(f"{book.title} by {book.author.name} ({book.genre.name})")

if __name__ == "__main__":
    cli()
