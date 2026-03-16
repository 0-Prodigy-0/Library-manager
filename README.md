# Home Library CLI

A command-line personal library manager that lets you track your book collection and reading progress, stored locally in a JSON file.

---

## Features

- Add books via a simple formatted string input
- Remove books by title (with partial match support)
- Search books by title, author, or genre
- View your entire library
- Mark books as read
- Track reading progress (% of books read)
- Supports regular Books and EBooks
- Data persists in a local `library.json` file

---

## Requirements

- Python 3.6+
- No external libraries required (uses built-in `json` and `os`)

---

## Usage

Run the script from your terminal:

```bash
python library.py
```

You'll be presented with a menu:

```
HOME LIBRARY
1. Add Book
2. Remove Book
3. Search Book
4. View Books
5. Mark book as read
6. Exit
```

---

## How It Works

| Option | Description |
|--------|-------------|
| **Add Book** | Enter book details in the format below to add to your library |
| **Remove Book** | Enter a title to remove — supports partial matches with confirmation |
| **Search Book** | Search across title, author, and genre fields |
| **View Books** | Displays all books with their details and read status |
| **Mark as Read** | Search for a book by title and mark it as read |
| **Exit** | Closes the program |

### Adding a Book

When adding a book, enter details in this exact format:

```
title | author | pages | genre
```

Example:
```
harry potter and the sorcerers stone | J.K. rowling | 400 | Fiction
```

> Books are set to **Unread** by default when added.

---

## Classes

### `Book`
Represents a physical book.

| Attribute | Type | Description |
|-----------|------|-------------|
| `title` | str | Title of the book |
| `author` | str | Author's name |
| `pages` | int | Number of pages |
| `genre` | str | Book genre |
| `read` | bool | Read status (default: `False`) |

### `EBook(Book)`
Extends `Book` with two additional attributes:

| Attribute | Type | Description |
|-----------|------|-------------|
| `file_size` | any | File size of the ebook |
| `format` | str | File format (e.g. PDF, EPUB) |

### `Library`
Manages the collection of books and handles all file I/O.

| Method | Description |
|--------|-------------|
| `save_book(book)` | Adds a book if it doesn't already exist |
| `remove(title)` | Removes a book by title |
| `search(query)` | Returns a list of matching books |
| `set_read(query)` | Marks a matching book as read |
| `progress` | Property — returns % of books read as a decimal |

---

## Data Storage

Books are saved in a `library.json` file in the **same directory as the script**, created automatically on first run.

Example format:

```json
{
    "books": [
        {
            "title": "harry potter and the sorcerers stone",
            "author": "J.K. rowling",
            "pages": 400,
            "genre": "Fiction",
            "read": true
        }
    ]
}
```

---

## Project Structure

```
library.py        # Main script
library.json      # Auto-generated library data file
README.md         # This file
```
