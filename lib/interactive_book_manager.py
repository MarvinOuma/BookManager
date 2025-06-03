import click
from lib.main import session, Author, Genre, Book, Publisher

def select_book():
    books = session.query(Book).all()
    if not books:
        click.echo("No books available.")
        return None
    book_titles = [f"{book.title} by {book.author.name} ({book.genre.name})" for book in books]
    for i, title in enumerate(book_titles, 1):
        click.echo(f"{i}. {title}")
    choice = click.prompt("Select a book by number", type=click.IntRange(1, len(book_titles)))
    return books[choice - 1]

def search_books():
    query = click.prompt("Enter search term (title, author, or genre)", type=str).strip()
    if not query:
        click.echo("Search term cannot be empty.")
        return
    books = session.query(Book).join(Author).join(Genre).filter(
        (Book.title.ilike(f"%{query}%")) |
        (Author.name.ilike(f"%{query}%")) |
        (Genre.name.ilike(f"%{query}%"))
    ).all()
    if not books:
        click.echo("No books found matching the search criteria.")
        return
    click.echo("Search results:")
    for book in books:
        click.echo(f"{book.title} by {book.author.name} ({book.genre.name})")

def add_book():
    title = click.prompt("Enter book title", type=str)
    author_name = click.prompt("Enter author name", type=str)
    genre_name = click.prompt("Enter genre name", type=str)

    if not title.strip() or not author_name.strip() or not genre_name.strip():
        click.echo("Error: Title, author name, and genre name must not be empty.")
        return

    author = session.query(Author).filter_by(name=author_name).first()
    if not author:
        author = Author(name=author_name)
        session.add(author)
        session.commit()
    genre = session.query(Genre).filter_by(name=genre_name).first()
    if not genre:
        genre = Genre(name=genre_name)
        session.add(genre)
        session.commit()

    existing_book = session.query(Book).filter_by(title=title, author=author, genre=genre).first()
    if existing_book:
        click.echo(f"Error: Book '{title}' by '{author_name}' in genre '{genre_name}' already exists.")
        return

    book = Book(title=title, author=author, genre=genre)
    session.add(book)
    session.commit()
    click.echo(f"Added book: {title}")

def list_books():
    books = session.query(Book).all()
    if not books:
        click.echo("No books found.")
        return
    for i, book in enumerate(books, 1):
        click.echo(f"{i}. {book.title} by {book.author.name} ({book.genre.name})")

def delete_book():
    book = select_book()
    if not book:
        return
    confirm = click.confirm(f"Are you sure you want to delete '{book.title}' by {book.author.name}?")
    if confirm:
        session.delete(book)
        session.commit()
        click.echo(f"Deleted book: {book.title}")
    else:
        click.echo("Delete cancelled.")

def update_book():
    book = select_book()
    if not book:
        return
    click.echo("Press enter without typing to keep the current value.")
    new_title = click.prompt(f"Enter new title [{book.title}]", default=book.title, show_default=False)
    new_author_name = click.prompt(f"Enter new author [{book.author.name}]", default=book.author.name, show_default=False)
    new_genre_name = click.prompt(f"Enter new genre [{book.genre.name}]", default=book.genre.name, show_default=False)
    new_publication_year = click.prompt(f"Enter new publication year [{book.publication_year or ''}]", default=book.publication_year or "", show_default=False)
    new_publisher_name = click.prompt(f"Enter new publisher [{book.publisher.name if book.publisher else ''}]", default=book.publisher.name if book.publisher else "", show_default=False)

    if not new_title.strip() or not new_author_name.strip() or not new_genre_name.strip():
        click.echo("Error: Title, author name, and genre name must not be empty.")
        return

    author = session.query(Author).filter_by(name=new_author_name).first()
    if not author:
        author = Author(name=new_author_name)
        session.add(author)
        session.commit()
    genre = session.query(Genre).filter_by(name=new_genre_name).first()
    if not genre:
        genre = Genre(name=new_genre_name)
        session.add(genre)
        session.commit()

    publisher = None
    if new_publisher_name.strip():
        publisher = session.query(Publisher).filter_by(name=new_publisher_name).first()
        if not publisher:
            publisher = Publisher(name=new_publisher_name)
            session.add(publisher)
            session.commit()

    pub_year = None
    if new_publication_year:
        try:
            pub_year = int(new_publication_year)
        except ValueError:
            click.echo("Invalid publication year. Skipping.")

    book.title = new_title
    book.author = author
    book.genre = genre
    book.publication_year = pub_year
    book.publisher = publisher
    session.commit()
    click.echo(f"Updated book: {book.title}")

def select_publisher():
    publishers = session.query(Publisher).all()
    if not publishers:
        click.echo("No publishers available.")
        return None
    for i, publisher in enumerate(publishers, 1):
        click.echo(f"{i}. {publisher.name}")
    choice = click.prompt("Select a publisher by number", type=click.IntRange(1, len(publishers)))
    return publishers[choice - 1]

def delete_publisher():
    publisher = select_publisher()
    if not publisher:
        return
    confirm = click.confirm(f"Are you sure you want to delete publisher '{publisher.name}'? This will also remove the publisher from any books.")
    if confirm:
        # Remove publisher from books
        books = session.query(Book).filter(Book.publisher == publisher).all()
        for book in books:
            book.publisher = None
        session.delete(publisher)
        session.commit()
        click.echo(f"Deleted publisher: {publisher.name}")
    else:
        click.echo("Delete cancelled.")

def manage_publishers():
    while True:
        click.echo("\nPublisher Management:")
        click.echo("1. Add publisher")
        click.echo("2. List publishers")
        click.echo("3. Delete publisher")
        click.echo("4. Back to main menu")
        choice = click.prompt("Enter choice", type=click.IntRange(1,4))
        if choice == 1:
            add_publisher()
        elif choice == 2:
            list_publishers()
        elif choice == 3:
            delete_publisher()
        elif choice == 4:
            break

def add_publisher():
    name = click.prompt("Enter publisher name")
    publisher = session.query(Publisher).filter_by(name=name).first()
    if publisher:
        click.echo("Publisher already exists.")
        return
    publisher = Publisher(name=name)
    session.add(publisher)
    session.commit()
    click.echo(f"Added publisher: {name}")

def list_publishers():
    publishers = session.query(Publisher).all()
    if not publishers:
        click.echo("No publishers found.")
        return
    for i, publisher in enumerate(publishers, 1):
        click.echo(f"{i}. {publisher.name}")

def main_menu():
    click.echo("\n\x1b[1m\x1b[4mBOOK MANAGER CLI\x1b[0m\n")  # Bold and underlined heading
    while True:
        click.echo("\nSelect an option:")
        click.echo("1. Add book")
        click.echo("2. List books")
        click.echo("3. Search books")
        click.echo("4. Delete book")
        click.echo("5. Update book")
        click.echo("6. Manage publishers")
        click.echo("7. Exit")
        choice = click.prompt("Enter choice", type=click.IntRange(1,7))
        if choice == 1:
            add_book()
        elif choice == 2:
            list_books()
        elif choice == 3:
            search_books()
        elif choice == 4:
            delete_book()
        elif choice == 5:
            update_book()
        elif choice == 6:
            manage_publishers()
        elif choice == 7:
            click.echo("Exiting Book Manager. Goodbye!")
            break

if __name__ == "__main__":
    main_menu()
