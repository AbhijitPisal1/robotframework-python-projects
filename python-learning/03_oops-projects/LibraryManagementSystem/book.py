# book.py
"""
This file defines the Book class and its subclasses to represent different types of books.
We implement Abstraction and Encapsulation here.

Abstraction is used to define a base class, and Encapsulation is used to restrict direct access to attributes.
"""

class Book:
    """Base class for all types of books."""

    def __init__(self, title, author, book_type):
        self.__title = title  # Encapsulation: Private attribute for book title
        self.__author = author  # Encapsulation: Private attribute for book author
        self.__book_type = book_type  # Encapsulation: Private attribute for book type

    # Abstract method for getting book details
    def get_details(self):
        return f"{self.__title} by {self.__author} ({self.__book_type})"


class Fiction(Book):
    """Class representing fiction books."""

    def __init__(self, title, author):
        super().__init__(title, author, "Fiction")


class NonFiction(Book):
    """Class representing non-fiction books."""

    def __init__(self, title, author):
        super().__init__(title, author, "Non-Fiction")


class Digital(Book):
    """Class representing digital books."""

    def __init__(self, title, author):
        super().__init__(title, author, "Digital")