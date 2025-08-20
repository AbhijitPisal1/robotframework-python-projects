# stack_array_fixed.py
# Fixed-size Stack (LIFO) implementation using a Python list.
# Note: This code snippet is adapted from an online Udemy tutorial for learning purposes.

class Stack:
    """A stack with a fixed maximum size, implemented using a Python list."""

    def __init__(self, maxSize):
        self.maxSize = maxSize
        self.list = []

    def __str__(self):
        """String representation of the stack (top at the top)."""
        if self.isEmpty():
            return "Stack is empty"
        return '\n'.join(map(str, reversed(self.list)))  # top at the top

    def isEmpty(self):
        """Check if the stack is empty."""
        return self.list == []

    def isFull(self):
        """Check if the stack has reached its max size."""
        return len(self.list) == self.maxSize

    def push(self, value):
        """Add a value to the top of the stack if it's not full."""
        if self.isFull():
            return "The stack is full"
        self.list.append(value)
        return "The element has been successfully inserted"

    def pop(self):
        """Remove and return the top value from the stack."""
        if self.isEmpty():
            return "There is not any element in the stack"
        return self.list.pop()

    def peek(self):
        """Return the top value without removing it."""
        if self.isEmpty():
            return "There is not any element in the stack"
        return self.list[-1]

    def delete(self):
        """Delete the entire stack."""
        self.list = None


# Example usage
customStack = Stack(4)
print(customStack.isEmpty())  # True
print(customStack.isFull())   # False

customStack.push(1)
customStack.push(2)
customStack.push(3)

print(customStack)
# Output:
# 3
# 2
# 1
