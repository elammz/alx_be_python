class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"Book: {self.title} by {self.author}"

    def __repr__(self):
        return f"Book('{self.title}', '{self.author}')"

class EBook(Book):
    def __init__(self, title, author, file_size_kb):
        super().__init__(title, author)  # Corrected: use __init__
        self.file_size_kb = file_size_kb

    def __str__(self):
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size_kb}KB"

    def __repr__(self):
        return f"EBook('{self.title}', '{self.author}', {self.file_size_kb})"

class PrintBook(Book):
    def __init__(self, title, author, page_count):
        super().__init__(title, author)  
        self.page_count = page_count

    def __str__(self):
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"

    def __repr__(self):
        return f"PrintBook('{self.title}', '{self.author}', {self.page_count})"

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def list_books(self):
        for book in self.books:
            print(book)

    def __repr__(self):
        return f"Library({self.books!r})"