# abstraction_runner.py
"""
This is the runner file to demonstrate Abstraction in the Library Management System.
It will show how book details can be fetched without exposing internals.
"""

from book import Fiction, NonFiction, Digital

# Create different book instances
book1 = Fiction("1984", "George Orwell")
book2 = NonFiction("Sapiens", "Yuval Noah Harari")
book3 = Digital("Digital Minimalism", "Cal Newport")

# Fetch details using the abstract method get_details
print(book1.get_details())
print(book2.get_details())
print(book3.get_details())