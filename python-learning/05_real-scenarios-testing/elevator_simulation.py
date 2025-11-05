"""
Problem Statement:
------------------
Design a class `Elevator` that simulates a simple elevator.

Implement:
- go_to(floor: int): Moves elevator to the given floor.
- current_floor(): Returns the current floor.
- reset(): Returns elevator to the ground floor (0).

What it tests:
--------------
- Class state management.
- Conditional logic and method interaction.
"""

class Elevator:
    def __init__(self):
        self.floor = 0

    def go_to(self, floor: int):
        """Move elevator to the specified floor."""
        if floor < 0:
            print("Invalid floor! Must be >= 0.")
            return
        print(f"Moving from floor {self.floor} to floor {floor}...")
        self.floor = floor
        print(f"Arrived at floor {self.floor}.")

    def current_floor(self) -> int:
        """Return the current floor number."""
        return self.floor

    def reset(self):
        """Return elevator to ground floor."""
        print(f"Resetting elevator from floor {self.floor} to 0.")
        self.floor = 0


# Example usage
if __name__ == "__main__":
    e = Elevator()
    e.go_to(5)
    print(e.current_floor())  # Output: 5
    e.reset()
    print(e.current_floor())  # Output: 0
