# composition_runner.py
"""
This is the runner file to demonstrate Composition in the E-Commerce System.
It showcases how an Order is composed of a ShoppingCart and products.
"""

from customer import RegularCustomer
from product import Electronics, Clothing
from order import Order

# Create a customer and order instance
customer = RegularCustomer("Alice", "alice@example.com")
order = Order(customer)

# Create product instances
product1 = Electronics("Smartphone", 699, 2)
product2 = Clothing("T-Shirt", 19.99, "M")

# Add products to the order
order.add_to_cart(product1)
order.add_to_cart(product2)

# Get order details
print(order.get_order_details())  # Print order details including customer and cart info