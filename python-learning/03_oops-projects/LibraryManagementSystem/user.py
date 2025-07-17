# user.py
"""
This file defines the User class and its subclasses to represent different types of users.
We demonstrate Inheritance and Encapsulation in this file.
"""


class User:
    """Base class for all users of the library."""

    def __init__(self, name, user_type):
        self.__name = name  # Encapsulation: Assigns the value of 'name' to the private attribute '__name'.
        self.__user_type = user_type  # Encapsulation: Private attribute for user type
        """By storing name as a private attribute, we ensure that external classes or functions cannot modify it 
        directly. This protects the internal state of the object and allows for controlled access through public 
        methods"""

    def get_details(self):
        """Get user details."""
        return f"{self.__name} ({self.__user_type})"


class Admin(User):
    """Class representing admin users."""

    def __init__(self, name):
        super().__init__(name, "Admin")     # Using super() to call the User constructor
        """super() function is used to call the constructor of the parent class. This allows the subclass to inherit 
        properties and methods from the parent class, maintaining a clear hierarchy and avoiding redundancy."""


class Student(User):
    """Class representing student users."""

    def __init__(self, name):
        super().__init__(name, "Student")       # Using super() to call the User constructor