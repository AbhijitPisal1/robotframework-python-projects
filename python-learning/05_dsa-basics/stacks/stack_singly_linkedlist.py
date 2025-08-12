# stack_singly_linkedlist.py
# Stack (LIFO) implementation using a singly linked list.
# Note: This code snippet is adapted from an online Udemy tutorial for learning purposes.

class Node:
    """A node in the singly linked list."""
    def __init__(self, value=None):
        self.value = value
        self.next = None

class LinkedList:
    """A singly linked list to store stack elements."""
    def __init__(self):
        self.head = None

    def __iter__(self):
        curNode = self.head
        while curNode:
            yield curNode
            curNode = curNode.next

class Stack:
    """A stack implemented using a singly linked list."""
    def __init__(self):
        self.LinkedList = LinkedList()

    def __str__(self):
        """String representation of the stack (top to bottom)."""
        values = [str(x.value) for x in self.LinkedList]
        return '\n'.join(values)

    def isEmpty(self):
        """Check if the stack is empty."""
        return self.LinkedList.head is None

    def push(self, value):
        """Push a new value onto the stack."""
        node = Node(value)
        node.next = self.LinkedList.head
        self.LinkedList.head = node

    def pop(self):
        """Remove and return the top element of the stack."""
        if self.isEmpty():
            return "There is not any element in the stack"
        nodeValue = self.LinkedList.head.value
        self.LinkedList.head = self.LinkedList.head.next
        return nodeValue

    def peek(self):
        """Return the top element without removing it."""
        if self.isEmpty():
            return "There is not any element in the stack"
        return self.LinkedList.head.value

    def delete(self):
        """Delete all elements in the stack."""
        self.LinkedList.head = None


# Example usage:
customStack = Stack()
customStack.push(1)
customStack.push(2)
customStack.push(3)

print(customStack.peek())  # Output: 3
print(customStack)         # Output: 3\n2\n1
