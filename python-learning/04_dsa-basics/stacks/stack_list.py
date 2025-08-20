# stack_list.py
# Simple Stack (LIFO) implementation using a Python list.
# Note: This code snippet is adapted from an online Udemy tutorial for learning purposes.

class Stack:
    """A basic stack implementation using Python's built-in list."""

    def __init__(self):
        self.items = []

    def push(self, element):
        """Add an element to the top of the stack."""
        self.items.append(element)

    def pop(self):
        """Remove and return the top element of the stack."""
        if self.is_empty():
            return "Stack is empty"
        return self.items.pop()

    def peek(self):
        """Return the top element without removing it."""
        if self.is_empty():
            return "Stack is empty"
        return self.items[-1]

    def is_empty(self):
        """Check whether the stack is empty."""
        return len(self.items) == 0

    def size(self):
        """Return the number of elements in the stack."""
        return len(self.items)

    def clear(self):
        """Remove all elements from the stack."""
        self.items = []

    def __str__(self):
        """String representation of the stack (top to bottom)."""
        if self.is_empty():
            return "Stack is empty"
        return '\n'.join(map(str, reversed(self.items)))  # top of stack on top


# Example usage
my_stack = Stack()
my_stack.push(5)
my_stack.push(8)
my_stack.push(9)
my_stack.push(10)

print(my_stack)  # Output: 10\n9\n8\n5

# Additional operations (Uncomment to test)
# print(my_stack.peek())     # Output: 10
# my_stack.pop()
# print(my_stack.peek())     # Output: 9
# print(my_stack.is_empty()) # Output: False
# print(my_stack.size())     # Output: 3
# my_stack.clear()
# print(my_stack.is_empty()) # Output: True
