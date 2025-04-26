# product.py
"""
This file defines the Product class and subclasses for different categories of products.
We demonstrate Abstraction and Encapsulation here.

Abstraction is used to define a base class, and Encapsulation is used to restrict direct access to attributes.
"""


class Product:
    """Base class for all Products in the e-commerce system."""

    def __init__(self, name, price):
        self.__name = name  # Encapsulation: Private attribute for product name
        self.__price = price  # Encapsulation: Private attribute for product price

    def get_details(self):
        """Abstract method to get product details."""
        return f"Product: {self.__name}, Price: ${self.__price}"


class Electronics(Product):
    """Class representing electronic products."""

    def __init__(self, name, price, warranty):
        super().__init__(name, price)  # Inheritance: Call the constructor of the Product class
        self.__warranty = warranty  # Encapsulation: Private attribute for warranty period

    def get_details(self):
        """Get details of the electronic product."""
        return f"{super().get_details()}, Warranty: {self.__warranty} years"


class Clothing(Product):
    """Class representing clothing products."""

    def __init__(self, name, price, size):
        super().__init__(name, price)  # Inheritance: Call the constructor of the Product class
        self.__size = size  # Encapsulation: Private attribute for clothing size

    def get_details(self):
        """Get details of the clothing product."""
        return f"{super().get_details()}, Size: {self.__size}"