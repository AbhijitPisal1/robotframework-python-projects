# library.py
"""
This file defines the Library class to manage books and users, demonstrating Polymorphism and Encapsulation.
Polymorphism is used in the borrowing and returning functions with different book types.
"""

from datetime import datetime


class Library:
    """Class to manage the library's collection of books and users."""

    def __init__(self):
        self.__books = []  # Encapsulation: Private attribute for the list of books
        self.__users = []  # Encapsulation: Private attribute for the list of users

    def add_book(self, book):
        """Adds a new book to the library."""
        self.__books.append(book)  # Encapsulation: Modifying the private book list

    def add_user(self, user):
        """Adds a new user to the library."""
        self.__users.append(user)  # Encapsulation: Modifying the private user list

    def borrow_book(self, book_title, user):
        """Borrow a book based on the title and the user."""
        for book in self.__books:
            if book.get_details().startswith(book_title):
                return f"{user.get_details()} has borrowed {book_title}"
        return "Book not found."

    def return_book(self, book_title, user):
        """Return a borrowed book based on the title and the user."""
        # Here we just acknowledge book return in a simplified way
        return f"{user.get_details()} has returned {book_title}"