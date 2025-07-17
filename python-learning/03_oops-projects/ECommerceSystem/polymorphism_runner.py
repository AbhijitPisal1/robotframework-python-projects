# polymorphism_runner.py
"""
This is the runner file to demonstrate Polymorphism in the E-Commerce System.
It tests the payment processing for different payment methods.
"""

from payment import CreditCardPayment, PayPalPayment

# Create payment method instances
credit_card_payment = CreditCardPayment()
paypal_payment = PayPalPayment()

# Simulate processing payments
print(credit_card_payment.process_payment(100.00))  # Test credit card payment
print(paypal_payment.process_payment(150.50))  # Test PayPal payment