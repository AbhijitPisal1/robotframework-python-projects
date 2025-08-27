from abc import ABC, abstractmethod

class PaymentGateway(ABC):
    @abstractmethod
    def authenticate(self, user_id):
        pass
        # No implementation here — this is a placeholder method
        # Subclasses MUST override this method with their own code
        #purpose is to force subclasses to implement these methods — serving as a strict blueprint or interface.
        # Without these abstract methods, subclasses might skip important method implementations, breaking the design.

    @abstractmethod
    def pay(self, amount):
        pass

class StripePayment(PaymentGateway):
    def authenticate(self, user_id):
        print(f"Authenticating user {user_id} with Stripe")

    def pay(self, amount):
        print(f"Processing payment of ${amount} through Stripe")

class PayPalPayment(PaymentGateway):
    def authenticate(self, user_id):
        print(f"Authenticating user {user_id} with PayPal")

    def pay(self, amount):
        print(f"Processing payment of ${amount} through PayPal")


# Usage
def process_payment(payment_gateway: PaymentGateway, user_id, amount):
    payment_gateway.authenticate(user_id)
    payment_gateway.pay(amount)

process_payment(StripePayment(), "user123", 150)
process_payment(PayPalPayment(), "user456", 200)

"""
Interface is a contract that defines methods a class must implement, without providing the method implementations itself. In Python, interfaces are commonly created using abstract base classes with abstract methods.

This concept is closely related to Abstraction because it hides the implementation details and only exposes method signatures. An interface ensures that different classes adhere to the same protocol or set of behaviors, which helps build flexible and extensible systems.

For example, a PaymentGateway interface defines methods like authenticate() and pay() that any payment method class must implement. This allows writing generic code (like process_payment) that can work with any payment gateway without caring about the specifics.

Interfaces are useful when you want to enforce certain behavior across different classes and enable polymorphism, allowing objects to be used interchangeably if they follow the same interface.
"""