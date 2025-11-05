import datetime

class BankAccount:
    def __init__(self, owner, pin, balance=0):
        self.owner = owner
        self.__pin = pin                    # private: cannot be accessed directly
        self.__balance = balance            # private balance
        self.__transactions = []            # private transaction log
        self.__daily_withdrawal_limit = 1000
        self.__withdrawn_today = 0
        self.__last_withdraw_date = None

    # --- Private method to log transactions ---
    def __log_transaction(self, type_, amount):
        self.__transactions.append({
            "type": type_,
            "amount": amount,
            "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        })

    # --- Deposit method (encapsulated logic) ---
    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.__balance += amount
        self.__log_transaction("DEPOSIT", amount)
        print(f"💰 {amount} deposited. New balance: ${self.__balance:.2f}")

    # --- Withdraw method (with business logic + PIN validation) ---
    def withdraw(self, amount, pin):
        today = datetime.date.today()
        if self.__last_withdraw_date != today:
            self.__withdrawn_today = 0
            self.__last_withdraw_date = today

        if pin != self.__pin:
            raise PermissionError("Invalid PIN.")
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self.__balance:
            raise ValueError("Insufficient funds.")
        if self.__withdrawn_today + amount > self.__daily_withdrawal_limit:
            raise ValueError("Daily withdrawal limit exceeded.")

        self.__balance -= amount
        self.__withdrawn_today += amount
        self.__log_transaction("WITHDRAW", amount)
        print(f"🏧 {amount} withdrawn. Remaining balance: ${self.__balance:.2f}")

    # --- Safe read-only property for balance ---
    @property
    def balance(self):
        return self.__balance

    # --- Method to view transaction history ---
    def get_statement(self, pin):
        if pin != self.__pin:
            raise PermissionError("Invalid PIN.")
        print(f"\n📜 Transaction History for {self.owner}:")
        for txn in self.__transactions:
            print(f"{txn['timestamp']}: {txn['type']} ${txn['amount']}")
        print(f"Current Balance: ${self.__balance:.2f}")

# --- Usage Example ---
acc = BankAccount("Alice", pin=4321, balance=1500)

acc.deposit(500)
acc.withdraw(200, pin=4321)
acc.withdraw(300, pin=4321)

print("\nChecking balance safely:")
print(acc.balance)  # ✅ Works via property
# print(acc.__balance)  # ❌ Raises AttributeError — encapsulated!

acc.get_statement(pin=4321)


"""
| Concept              | Implementation                                                                     |
| -------------------- | ---------------------------------------------------------------------------------- |
| **Encapsulation**    | `__balance`, `__pin`, and `__transactions` are private; can’t be touched directly. |
| **Data Protection**  | Only controlled methods (`deposit`, `withdraw`) can change balance.                |
| **Validation Rules** | PIN check, withdrawal limit, positive amounts — all handled inside methods.        |
| **Audit Trail**      | Every change is logged privately — the user can’t edit it, only view.              |
| **Safe Access**      | `.balance` is a *read-only property*, protecting internal state.                   |

"""