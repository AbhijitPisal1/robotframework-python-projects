# stack_array_basic.py
# Simple Stack (LIFO) implementation using a Python list.
# Note: This code snippet is adapted from an online Udemy tutorial for learning purposes.

class Stack:
    """A stack data structure implemented using Python's built-in list."""
    
    def __init__(self):
        self.list = []

    def __str__(self):
        """String representation of the stack (top at the top)."""
        return '\n'.join(map(str, reversed(self.list))) if self.list else "Stack is empty"

    def isEmpty(self):
        """Check whether the stack is empty."""
        return self.list == []

    def push(self, value):
        """Push a value onto the top of the stack."""
        self.list.append(value)
        return "The element has been successfully inserted"

    def pop(self):
        """Pop and return the top value from the stack."""
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
customStack = Stack()
customStack.push(1)
customStack.push(2)
customStack.push(3)

print(customStack.peek())   # Output: 3
print(customStack)          # Output: 3\n2\n1
