# inheritance_runner.py
"""
This is the runner file to demonstrate Inheritance in the Library Management System.
It showcases adding different types of books and users.
"""

from library import Library
from book import Fiction, NonFiction, Digital
from user import Admin, Student

# Create library instance
my_library = Library()

# Create different types of books
book1 = Fiction("1984", "George Orwell")
book2 = NonFiction("Sapiens", "Yuval Noah Harari")
book3 = Digital("Digital Minimalism", "Cal Newport")

# Add books to library
my_library.add_book(book1)
my_library.add_book(book2)
my_library.add_book(book3)

# Create different types of users
admin_user = Admin("Alice")
student_user = Student("Bob")

# Add users to library
my_library.add_user(admin_user)
my_library.add_user(student_user)

# Show added books and users
print(f"Books in library: {[book.get_details() for book in my_library._Library__books]}")
print(f"Users in library: {[user.get_details() for user in my_library._Library__users]}")