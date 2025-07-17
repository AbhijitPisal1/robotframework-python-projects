# encapsulation_runner.py
"""
This is the runner file to demonstrate Encapsulation in the E-Commerce System.
It shows how private attributes are managed within the classes.
"""

from customer import Customer

# Attempt to create a customer
customer = Customer("Alice", "alice@example.com")

# Accessing details using the getter (we can assume getters exist like get_details)
print(customer.get_details())  # Should print customer details