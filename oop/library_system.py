class Book:
    def __init__(self, title:str, author:str ):
        self.tittle = tittle
        self.author = author

    def __str__(self):
        return f"Book: {self.title} by {self.author}"
class Ebook(Book):
    def __init__(self, title: str, author: str, file_size):
        super().__init__(title, author)
        self.file_size = file_size

    def __str__(self):
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"
class PrintBook(Book):
    def __init__(self, title: str, author: str, page_count):
        super().__init__(title, author)
        self.page_count = page_count

    def __str__(self):
        return f"PrintBook: {self.title} by {self.author}, File Size: {self.page_count}KB"
class Library:
    def __init__(self):
        self.books = []
    def add_book(self, book):
        self.books.append(book)
    def list_book(self):
        for book in self.books:
            print(book)
