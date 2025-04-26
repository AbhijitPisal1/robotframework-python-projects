# cart.py
"""
This file defines the ShoppingCart class which manages products in the cart.
Demonstrates Composition as the cart is composed of Product objects.
"""

from product import Product


class ShoppingCart:
    """Class representing a shopping cart."""

    def __init__(self):
        self.__items = []  # Encapsulation: Private list for storing Product objects

    def add_product(self, product):
        """Add a product to the shopping cart."""
        if isinstance(product, Product):  # Check if the product is an instance of Product
            self.__items.append(product)  # Add product to the items list

    def get_total_price(self):
        """Calculate total price of items in the cart."""
        total = sum([product._Product__price for product in self.__items])  # Accessing price via convention
        return total

    def get_cart_details(self):
        """Get details of all items in the cart."""
        return [product.get_details() for product in self.__items]