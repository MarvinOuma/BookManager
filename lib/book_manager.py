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
    if not title.strip() or not author_name.strip() or not genre_name.strip():
        click.echo("Error: Title, author name, and genre name must not be empty.")
        raise click.Abort()
    author = session.query(Author).filter_by(name=author_name).first()
    if not author:
        author = Author(name=author_name)
    genre = session.query(Genre).filter_by(name=genre_name).first()
    if not genre:
        genre = Genre(name=genre_name)
    # Check for duplicate book
    existing_book = session.query(Book).filter_by(title=title, author=author, genre=genre).first()
    if existing_book:
        click.echo(f"Error: Book '{title}' by '{author_name}' in genre '{genre_name}' already exists.")
        raise click.Abort()
    book = Book(title=title, author=author, genre=genre)
    session.add(book)
    session.commit()
    click.echo(f"Added book: {title}")

@cli.command()
def list():
    books = session.query(Book).all()
    for book in books:
        print(f"{book.title} by {book.author.name} ({book.genre.name})")

@cli.command()
@click.argument("title")
def delete(title):
    book = session.query(Book).filter_by(title=title).first()
    if not book:
        click.echo(f"No book found with title: {title}")
        return
    session.delete(book)
    session.commit()
    click.echo(f"Deleted book: {title}")

if __name__ == "__main__":
    cli()
