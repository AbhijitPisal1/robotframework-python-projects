# inheritance_runner.py
"""
This is the runner file to demonstrate Inheritance in the E-Commerce System.
It showcases creating different types of customers.
"""

from customer import RegularCustomer, PremiumCustomer

# Create customers
customer1 = RegularCustomer("Alice", "alice@example.com")
customer2 = PremiumCustomer("Bob", "bob@example.com")

# Show details and discounts for each customer type
print(customer1.get_details(), "Discount:", customer1.get_discount()*100, "%")  # Regular customer details
print(customer2.get_details(), "Discount:", customer2.get_discount()*100, "%")  # Premium customer details