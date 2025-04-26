# payment.py
"""
This file defines abstract classes for payment methods, demonstrating Abstraction and Polymorphism.
Different payment methods will implement their own versions of processing payments.
"""

from abc import ABC, abstractmethod


class PaymentMethod(ABC):
    """Abstract base class for payment methods."""

    @abstractmethod
    def process_payment(self, amount):
        """Abstract method to process a payment."""
        pass


class CreditCardPayment(PaymentMethod):
    """Concrete class for credit card payments."""

    def process_payment(self, amount):
        """Process payment via credit card."""
        return f"Processed credit card payment of ${amount}"


class PayPalPayment(PaymentMethod):
    """Concrete class for PayPal payments."""

    def process_payment(self, amount):
        """Process payment via PayPal."""
        return f"Processed PayPal payment of ${amount}"