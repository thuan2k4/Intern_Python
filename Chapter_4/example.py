class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def __str__(self):
        return f"{self.title} by {self.author} - ${self.price}"

class Library(Book):
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book):
        self.books.remove(book)

    def show_book(self):
        for book in self.books:
            print(book)

Book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", 10.99)
Book2 = Book("1984", "George Orwell", 12.99)

Library = Library()
Library.add_book(Book1)
Library.add_book(Book2)
Library.show_book()
