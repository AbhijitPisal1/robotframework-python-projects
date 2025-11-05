from abc import ABC, abstractmethod
import random
import time


# --- Abstract Payment Class ---
class PaymentMethod(ABC):
    @abstractmethod
    def pay(self, amount):
        pass


# --- Concrete Implementations ---
class CreditCard(PaymentMethod):
    def __init__(self, card_number, cvv):
        self.card_number = card_number
        self.cvv = cvv

    def pay(self, amount):
        print(f"🔹 Processing credit card payment of ${amount}...")
        time.sleep(1)
        if len(self.card_number) == 16 and len(self.cvv) == 3:
            fee = amount * 0.02
            print(f"✅ Credit Card payment approved! Fee: ${fee:.2f}")
            return True
        else:
            print("❌ Invalid credit card details.")
            return False


class PayPal(PaymentMethod):
    def __init__(self, email):
        self.email = email

    def pay(self, amount):
        print(f"🔹 Redirecting to PayPal for ${amount} payment...")
        time.sleep(1)
        if "@" in self.email:
            print("✅ PayPal payment successful!")
            return True
        else:
            print("❌ Invalid PayPal account.")
            return False


class Crypto(PaymentMethod):
    def __init__(self, wallet_address):
        self.wallet_address = wallet_address

    def pay(self, amount):
        print(f"🔹 Initiating crypto transaction of ${amount}...")
        time.sleep(1)
        confirmation_time = random.randint(2, 5)
        print(f"⏳ Waiting {confirmation_time} seconds for blockchain confirmation...")
        time.sleep(confirmation_time)
        print("✅ Crypto payment confirmed on blockchain.")
        return True


# --- Unified Payment Function ---
def make_payment(payment_method: PaymentMethod, amount):
    print("\n--- Starting Transaction ---")
    success = payment_method.pay(amount)
    if success:
        print("💰 Payment complete!\n")
    else:
        print("⚠️ Payment failed!\n")


# --- Usage ---
credit_card = CreditCard("1234567812345678", "123")
paypal = PayPal("user@example.com")
crypto = Crypto("0xAbC12345Def67890")

make_payment(credit_card, 100)
make_payment(paypal, 250)
make_payment(crypto, 500)


"""
Same interface: every payment type implements .pay(amount)
Different behavior: each one performs realistic operations
    CreditCard: validates card & charges with fee
    PayPal: simulates email-based payment
    Crypto: waits for blockchain confirmation
Polymorphism in action: the make_payment() function doesn’t care which payment method it’s handling — it just calls pay() and gets the result.
"""