# abstraction_runner.py
"""
This is the runner file to demonstrate Abstraction in the E-Commerce System.
It will show how product details can be fetched without exposing internals.
"""

from product import Electronics, Clothing

# Create product instances
product1 = Electronics("Smartphone", 699, 2)
product2 = Clothing("T-Shirt", 19.99, "M")

# Fetch details using the abstract method get_details
print(product1.get_details())  # Details of the electronic product
print(product2.get_details())  # Details of the clothing product