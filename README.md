# BookManager

This is a simple book management CLI application built with Python and SQLAlchemy. It allows you to add, list, delete, update books along with their authors, genres, publishers, and publication years.

## Features

- Add books with author, genre, publisher, and publication year information.
- List all books in the database.
- Search books by title, author, or genre.
- Update existing book entries.
- Delete books interactively.
- Manage publishers (add, list, delete).
- Seed the database with initial data.

## Setup

1. Create and activate a Python virtual environment.

2. Install dependencies using `pip install -r requirements.txt`.

3. Run database migrations using Alembic:

   ```bash
   alembic upgrade head
   ```

4. (Optional) Seed the database with initial data:

   ```bash
   python -m lib.seed
   ```

## Usage

Run the CLI commands using Python's module flag:

- Add a book:

  ```bash
  python -m lib.book_manager add "Book Title" "Author Name" "Genre Name"
  ```

- List all books:

  ```bash
  python -m lib.book_manager list
  ```

- Use the interactive CLI with a menu-driven interface:

  ```bash
  python -m lib.interactive_book_manager
  ```

  When you launch the interactive CLI, you will see a menu with numbered options:

  1. Add book  
  2. List books  
  3. Search books  
  4. Delete book  
  5. Update book  
  6. Manage publishers  
  7. Exit  

  You can enter the number corresponding to the action you want to perform. The search option allows you to find books by title, author, or genre. Publisher management lets you add, list, and delete publishers.

## Testing

Test the CLI commands by running them and verifying the output. The interactive CLI supports adding, listing, searching, updating, and deleting books with prompts, as well as managing publishers.

## Notes

- Ensure the database migrations are applied before running the CLI.
- The seed script (`lib/seed.py`) can be used to populate the database with sample data.

## Future Functionality

- Support exporting and importing book data in various formats (CSV, JSON).
- Add user authentication and permissions for multi-user support.
- Develop a web-based UI for easier interaction.
- Implement pagination for listing large numbers of books.
- Add detailed logging and error handling improvements.

## Coder

This project was developed by Marvin Daniel.  
GitHub: [https://github.com/MarvinOuma](https://github.com/MarvinOuma)
