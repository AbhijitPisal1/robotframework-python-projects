class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance  # Private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"{amount} deposited. New balance: {self.__balance}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"{amount} withdrawn. New balance: {self.__balance}")
        else:
            print("Insufficient funds or invalid amount.")

    def get_balance(self):
        return self.__balance


# Usage
acc = BankAccount("Alice", 1000)
acc.deposit(500)
acc.withdraw(200)
print("Current Balance:", acc.get_balance())

# Trying to access private balance directly (this will fail)
# print(acc.__balance)  # AttributeError

"""
Encapsulation – "Protect your data"

Encapsulation means hiding the internal state of an object from the outside world and only allowing access through methods. For example, in a bank account system, the balance shouldn't be directly modified from outside the class — it should be modified only through deposit and withdrawal methods.

This ensures the object stays in a valid state and helps prevent accidental misuse. It’s also easier to debug and refactor since all changes to the data go through a single point.

Use encapsulation when you have sensitive data or need control over how attributes are accessed or modified.
"""

