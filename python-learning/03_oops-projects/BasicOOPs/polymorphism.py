class PaymentMethod:
    def pay(self, amount):
        raise NotImplementedError("Subclass must implement this method")

class CreditCard(PaymentMethod):
    def pay(self, amount):
        print(f"Paying {amount} using Credit Card.")

class PayPal(PaymentMethod):
    def pay(self, amount):
        print(f"Paying {amount} using PayPal.")

class UPI(PaymentMethod):
    def pay(self, amount):
        print(f"Paying {amount} using UPI.")

# Unified payment function
def make_payment(payment_method, amount):
    payment_method.pay(amount)


# Usage
make_payment(CreditCard(), 1000)
make_payment(PayPal(), 500)
make_payment(UPI(), 300)

"""
Polymorphism – "Same interface, different behavior"

Polymorphism allows different objects to use the same method name, but each object performs its version of the action. For instance, all payment methods (Credit Card, PayPal, UPI) implement a pay() method, but the actual implementation differs.

This is powerful in systems where you want to process many types of objects with a common interface. You can write flexible code that doesn’t need to know the exact type of object it's working with — just that it knows how to behave.

Use polymorphism when you want to write generalized code that works with many different classes
"""