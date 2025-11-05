"""
Problem Statement:
------------------
You are building a simple order tracker for an online store.
Each order includes an `item_name` and a `quantity`.

Implement a class `OrderTracker` with the following methods:
- add_order(item: str, quantity: int): Adds the quantity to that item’s total.
- get_quantity(item: str): Returns how many units have been ordered for that item.
- total_items(): Returns the total number of all items ordered.

What it tests:
--------------
- Use of dictionaries for dynamic data storage.
- Loops, condition handling, and accumulation logic.
"""

class OrderTracker:
    def __init__(self):
        self.orders = {}

    def add_order(self, item: str, quantity: int):
        """Add a new order or increase existing quantity."""
        if quantity <= 0:
            print("Quantity must be positive.")
            return
        self.orders[item] = self.orders.get(item, 0) + quantity

    def get_quantity(self, item: str) -> int:
        """Return total quantity ordered for a specific item."""
        return self.orders.get(item, 0)

    def total_items(self) -> int:
        """Return total quantity of all ordered items."""
        return sum(self.orders.values())


# Example usage
if __name__ == "__main__":
    tracker = OrderTracker()
    tracker.add_order("Book", 3)
    tracker.add_order("Pen", 5)
    tracker.add_order("Book", 2)
    print(tracker.get_quantity("Book"))   # Output: 5
    print(tracker.total_items())          # Output: 8
