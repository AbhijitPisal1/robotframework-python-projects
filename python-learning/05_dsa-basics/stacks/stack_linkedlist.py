# stack_linkedlist.py
# Implementation of a Stack (LIFO) using a singly linked list.
# Note: This code snippet is adapted from an online Udemy tutorial for learning purposes.

class Node:
    """Node class to represent elements in the linked list stack."""
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    """LIFO stack implementation using a singly linked list."""
    def __init__(self):
        self.top = None    # Reference to the top node in the stack
        self.length = 0    # Number of elements in the stack

    def push(self, value):
        """Add a new value to the top of the stack."""
        new_node = Node(value)
        new_node.next = self.top  # Link new node to the current top
        self.top = new_node       # Update top reference
        self.length += 1

    def pop(self):
        """Remove and return the top node of the stack."""
        if self.top is None:
            return None  # Stack is empty
        popped_node = self.top
        self.top = self.top.next
        self.length -= 1
        return popped_node

    def peek(self):
        """Return the value at the top of the stack without removing it."""
        return self.top.value if self.top else None

    def is_empty(self):
        """Check whether the stack is empty."""
        return self.top is None

    def clear(self):
        """Remove all elements from the stack."""
        self.top = None
        self.length = 0

    def __len__(self):
        """Return the number of elements in the stack."""
        return self.length

    def __str__(self):
        """String representation of stack contents (top to bottom)."""
        current = self.top
        values = []
        while current:
            values.append(str(current.value))
            current = current.next
        return ' -> '.join(values)


# Example usage:
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)

print(stack)               # Output: 3 -> 2 -> 1
print(stack.pop())         # Output: <Node object at ...> (contains value 3)
print(stack.peek())        # Output: 2
print(stack.is_empty())    # Output: False
print(len(stack))          # Output: 2
