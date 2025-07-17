# customer.py
"""
This file defines the Customer class, demonstrating Encapsulation and Inheritance.
The Customer class manages customer data and registration.
"""


class Customer:
    """Base class for all customers in the e-commerce system."""

    def __init__(self, name, email):
        self.__name = name  # Encapsulation: Private attribute for customer name
        self.__email = email  # Encapsulation: Private attribute for customer email

    def get_details(self):
        """Get customer details."""
        return f"Customer: {self.__name}, Email: {self.__email}"


class RegularCustomer(Customer):
    """Class representing regular customers."""

    def __init__(self, name, email):
        super().__init__(name, email)  # Inheritance: Call the constructor of the Customer class

    def get_discount(self):
        """Method to get the discount for regular customers."""
        return 0.05  # 5% discount


class PremiumCustomer(Customer):
    """Class representing premium customers."""

    def __init__(self, name, email):
        super().__init__(name, email)  # Inheritance: Call the constructor of the Customer class

    def get_discount(self):
        """Method to get the discount for premium customers."""
        return 0.10  # 10% discount