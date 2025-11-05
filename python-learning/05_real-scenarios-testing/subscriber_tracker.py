"""
Problem Statement:
------------------
You are given an array of length 24, where each element represents the number of new subscribers 
during the corresponding hour of a day (0 to 23).

You need to implement a simple system that supports two operations:

1. update(hour: int, value: int):
   - Increment the element at index 'hour' by 'value'.
   - Example: update(3, 5) adds 5 new subscribers to hour 3.

2. query(start: int, end: int):
   - Retrieve the total number of subscribers that have signed up between 'start' and 'end' (inclusive).
   - Example: query(2, 5) returns the sum of subscribers from hour 2 to hour 5.

Assume:
- All data resets at midnight (i.e., the array is cleared back to zeros each new day).
- The implementation should use simple Python logic without any external packages.
"""

class SubscriberTracker:
    def __init__(self):
        # Initialize 24 hours of subscriber counts (all start at 0)
        self.subscribers = [0] * 24

    def update(self, hour: int, value: int):
        """Increment the number of subscribers for the given hour."""
        if 0 <= hour < 24:
            self.subscribers[hour] += value
        else:
            print("Invalid hour! Must be between 0 and 23.")

    def query(self, start: int, end: int) -> int:
        """Return the total subscribers from 'start' to 'end' hour (inclusive)."""
        if 0 <= start <= end < 24:
            return sum(self.subscribers[start:end + 1])
        else:
            print("Invalid range! Hours must be between 0 and 23.")
            return 0

    def reset_day(self):
        """Reset all subscriber data (simulate midnight reset)."""
        self.subscribers = [0] * 24


# Example usage:
if __name__ == "__main__":
    tracker = SubscriberTracker()
    tracker.update(3, 5)
    tracker.update(5, 10)
    tracker.update(3, 2)
    print(tracker.query(3, 5))  # Output: 17
    tracker.reset_day()
    print(tracker.query(0, 23))  # Output: 0
