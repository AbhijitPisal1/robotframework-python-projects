# Encapsulation:
# Restricts direct access to some object components (private variables),
# providing controlled access via methods (getters/setters) to protect data integrity.

class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance   # private variable

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient balance")

    def get_balance(self):
        return self.__balance

# Usage
acc = Account("Bob", 1000)
acc.deposit(500)
acc.withdraw(200)
print(acc.get_balance())  # 1300
#print(acc.__balance)     # AttributeError: 'Account' object has no attribute '__balance'
