import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_PATH = os.path.join(BASE_DIR, "library.json")

class  Library:
    def __init__(self):
        try:
            with open(FILE_PATH, "r") as f:
                self.data = json.load(f)
        except json.JSONDecodeError:
            print("File corrupt, resetting library")
            self.data = {"books": []}
            
        except FileNotFoundError:
            self.data = {"books": []}
            with open(FILE_PATH, 'w') as f:
                json.dump(self.data, f, indent = 4)
            print(f"Created file in {FILE_PATH}")

    def __len__(self):
        return len(self.data['books'])
    
    
    def save_book(self, book):
        if book.title in self:
            print("Book already exists")
            return False
        
        self.data['books'].append({
            "title": book.title,
            "author": book.author,
            "pages": book.pages,
            "genre": book.genre,
            "read": book.read,
        })

        with open(FILE_PATH, 'w') as f:
            json.dump(self.data, f, indent=4)
        return True

    def __contains__(self, title):
        for book in self.data['books']:
            if book['title'].lower() == title.lower():
                return True
        return False
    
    def remove(self, title):
        for book in self.data['books']:
            if book['title'].lower() == title.lower():
                self.data['books'].remove(book)
                with open(FILE_PATH, 'w') as f:
                    json.dump(self.data, f, indent=4)
                return True
            elif title.lower() in book['title'].lower():
                print(f"\n{book}")
                query = input("Now enter the full title of the book: ")
                if book['title'].lower() == query.lower():
                    self.data['books'].remove(book)
                    with open(FILE_PATH, 'w') as f:
                        json.dump(self.data, f, indent=4)
                    return True

        return False
    
    def search(self, query):
        results = []
        for book in self.data['books']:
            if (query.lower() in book['title'].lower() or
                query.lower() in book['author'].lower() or
                query.lower() in book['genre'].lower()):
                results.append(book)
        return results
    
    def __str__(self):
        if not self.data['books']:
            return "Library is empty"
        lines = []
        for book in self.data['books']:
            lines.append(f"{book['title']} by {book['author']} ({book['pages']} pages, {book['genre']}) - {'Read' if book['read'] else 'Unread'}")
        return "\n".join(lines)
    
    @property
    def progress(self):
        books_read  = 0 
        for book in self.data['books']:
            if book['read'] == True:
                books_read = books_read + 1
        progress_percent = books_read / len(self.data['books'])
        return progress_percent
    
    def set_read(self, query):
        for book in self.data['books']:
            if query.lower() in book['title'].lower():
                if book['read']:
                    return False
                book['read'] = True
                with open(FILE_PATH, 'w') as f:
                    json.dump(self.data, f, indent=4)
                print("Set book as read")
            print("Book already set to read")
        return False
    
    def __repr__(self):
        if not self.data['books']:
            return "Library(books=[])"
        lines = []
        for book in self.data['books']:
            lines.append(f"Book('{book['title']}', '{book['author']}', {book['pages']}, '{book['genre']}', {book['read']})")
        return f"Library(books=[{', '.join(lines)}])"
    

              
class Book:
    def __init__(self, title, author, pages, genre, read = False):
        self.title = title
        self.author = author
        self.pages = pages
        self.genre = genre
        self.read = read

    def __str__(self):
        return "{} by {} ({} pages, {}) - {}".format(self.title, self.author, self.pages, self.genre, 'Unread' if self.read == False else 'Read')

    def __repr__(self):
        return f"Book(title = {self.title}, author = {self.author}, pages = {self.pages}, genre = {self.genre}, read = {self.read})"
    
    @classmethod
    def from_string(cls, string):
        title, author, pages, genre = string.split(' | ')
        return cls(title, author, int(pages), genre)

class EBook(Book):
    def __init__(self, title, author, pages, genre, read, file_size, format):
        super().__init__(title, author, pages, genre, read)
        self.file_size = file_size
        self.format = format


def main():
    lib = Library()

    while True:
        print("HOME LIBRARY")
        print("1.Add Book")
        print("2.Remove Book")
        print("3.Search Book")
        print("4.View Books")
        print("5.Mark book as read")
        print("6.Exit")

        try:
            query = int(input("Enter the corresponding number of the action: "))
        except ValueError:
            print("Invalid input, please enter a number")
            return

        if query < 1 or query > 6:
            print("Invalid Input, out of range")
            return
        elif query == 1:
                book = Book.from_string(input("Enter the book details in this format exactly- book title | author | pages | genre\n-->"))
                lib.save_book(book)
                return 'Book added'
        elif query == 2:
                bk = input("Enter the title of the book: ")
                lib.remove(bk) 
        elif query == 3:
            print(lib.search(input("Enter the title, author or genre of the book: ")))
        elif query == 4:
            print(lib)
        elif query == 5:
            print(lib)
            lib.set_read(input("Enter the title of the book: "))
        elif query == 6:
            break
if __name__ == "__main__":
    main()
