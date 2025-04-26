# encapsulation_runner.py
"""
This is the runner file to demonstrate Encapsulation in the Library Management System.
It shows how private attributes are managed within the classes.
"""

from book import Book
from user import User

# Attempt to create a book and a user
book_item = Book("1984", "George Orwell", "Fiction")
user_item = User("Alice", "Student")

# Accessing details using the getter (we can assume getters exist like get_details)
print(user_item.get_details())  # Should print user details