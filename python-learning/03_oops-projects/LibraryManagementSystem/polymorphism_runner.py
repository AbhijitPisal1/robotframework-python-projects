# polymorphism_runner.py
"""
This is the runner file to demonstrate Polymorphism in the Library Management System.
It tests the borrow and return functionalities for different types of books.
"""

from library import Library
from book import Fiction, NonFiction, Digital
from user import Admin, Student

# Create library instance
my_library = Library()

# Create books
book1 = Fiction("1984", "George Orwell")
book2 = NonFiction("Sapiens", "Yuval Noah Harari")
book3 = Digital("Digital Minimalism", "Cal Newport")

# Add books to library
my_library.add_book(book1)
my_library.add_book(book2)
my_library.add_book(book3)

# Create users
admin_user = Admin("Alice")
student_user = Student("Bob")

# Add users to library
my_library.add_user(admin_user)
my_library.add_user(student_user)

# Test borrowing and returning books with Polymorphism
print(my_library.borrow_book("1984", student_user))  # Student borrows a fiction book
print(my_library.return_book("1984", student_user))  # Student returns the fiction book