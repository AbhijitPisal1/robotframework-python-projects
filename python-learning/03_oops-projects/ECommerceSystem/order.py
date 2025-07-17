# order.py
"""
This file defines the Order class which manages orders placed by customers.
It demonstrates Abstraction and Composition as it holds information about orders and products.
"""

from customer import Customer
from cart import ShoppingCart


class Order:
    """Class representing an order in the e-commerce system."""

    def __init__(self, customer):
        self.__customer = customer  # Encapsulation: Private attribute for the customer placing the order
        self.__cart = ShoppingCart()  # Composition: An Order contains a ShoppingCart

    def add_to_cart(self, product):
        """Add a product to the order's cart."""
        self.__cart.add_product(product)  # Add product to the cart

    def get_order_details(self):
        """Get details of the order, including customer and cart details."""
        return {
            "customer": self.__customer.get_details(),
            "cart": self.__cart.get_cart_details(),
            "total": self.__cart.get_total_price()
        }