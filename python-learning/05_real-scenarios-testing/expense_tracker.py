"""
Problem Statement:
------------------
You are building a simple daily expense tracker.

Each expense entry has:
- category (str)
- amount (float)

Implement:
- add_expense(category: str, amount: float)
- total_spent(): Returns total expenses.
- spent_by_category(category: str): Returns total spent in a given category.

What it tests:
--------------
- Lists and filtering logic.
- Summation and grouping using dictionaries.
"""

class ExpenseTracker:
    def __init__(self):
        self.expenses = []

    def add_expense(self, category: str, amount: float):
        """Add a new expense record."""
        if amount <= 0:
            print("Amount must be positive.")
            return
        self.expenses.append((category, amount))

    def total_spent(self) -> float:
        """Return total amount spent."""
        return sum(amount for _, amount in self.expenses)

    def spent_by_category(self, category: str) -> float:
        """Return total spent for a given category."""
        return sum(amount for cat, amount in self.expenses if cat == category)


# Example usage
if __name__ == "__main__":
    et = ExpenseTracker()
    et.add_expense("Food", 25.5)
    et.add_expense("Travel", 40.0)
    et.add_expense("Food", 15.0)
    print(et.total_spent())               # Output: 80.5
    print(et.spent_by_category("Food"))   # Output: 40.5
