"""
Doubly Linked List Implementation in Python

This file implements a doubly linked list (DLL) with basic operations like append,
prepend, insert, remove, search, traversal (forward and reverse), and complete deletion.

Note: This code snippet is adapted from an online Udemy tutorial for educational purposes.

Classes:
- Node: Represents a DLL node with value, next, and prev pointers.
- DoublyLinkedList: Manages DLL operations and maintains head, tail, and length.

Key methods:
- append(value): Adds a node to the end.
- prepend(value): Adds a node to the start.
- insert(index, value): Inserts a node at a specific index.
- remove(index): Removes node at a given index.
- pop_first(): Removes the first node.
- pop(): Removes the last node.
- get(index): Returns node at index (optimized to start from head or tail).
- set_value(index, value): Changes the value of a node at index.
- search(target): Returns the index of the node with the target value, or -1 if not found.
- traverse(): Prints values from head to tail.
- reverse_traverse(): Prints values from tail to head.
- delete_all(): Deletes the entire list.
"""

class Node:
    def __init__(self, value):
        self.value = value    # Data in node
        self.next = None      # Pointer to next node
        self.prev = None      # Pointer to previous node

    def __str__(self):
        return str(self.value)

class DoublyLinkedList:
    def __init__(self):
        self.head = None      # Start of DLL
        self.tail = None      # End of DLL
        self.length = 0       # Number of nodes

    def __str__(self):
        # Returns string representation like "1 <-> 2 <-> 3"
        temp_node = self.head
        result = ''
        while temp_node:
            result += str(temp_node.value)
            if temp_node.next:
                result += ' <-> '
            temp_node = temp_node.next
        return result

    def append(self, value):
        # Add node at end
        new_node = Node(value)
        if not self.head:  # Empty list
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1

    def prepend(self, value):
        # Add node at start
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1

    def traverse(self):
        # Print all values head to tail
        current_node = self.head
        while current_node:
            print(current_node.value)
            current_node = current_node.next

    def reverse_traverse(self):
        # Print all values tail to head
        current_node = self.tail
        while current_node:
            print(current_node.value)
            current_node = current_node.prev

    def search(self, target):
        # Return index of first occurrence of target, else -1
        current_node = self.head
        index = 0
        while current_node:
            if current_node.value == target:
                return index
            current_node = current_node.next
            index += 1
        return -1

    def get(self, index):
        # Return node at index, or None if out of range
        if index < 0 or index >= self.length:
            return None
        if index < self.length // 2:
            current_node = self.head
            for _ in range(index):
                current_node = current_node.next
        else:
            current_node = self.tail
            for _ in range(self.length - 1, index, -1):
                current_node = current_node.prev
        return current_node

    def set_value(self, index, value):
        # Set node value at index, return True if successful
        node = self.get(index)
        if node:
            node.value = value
            return True
        return False

    def insert(self, index, value):
        # Insert node at index, handle edge cases (start/end)
        if index < 0 or index > self.length:
            print("Error: Index out of bounds.")
            return
        if index == 0:
            self.prepend(value)
            return
        elif index == self.length:
            self.append(value)
            return
        new_node = Node(value)
        temp_node = self.get(index - 1)
        new_node.next = temp_node.next
        new_node.prev = temp_node
        temp_node.next.prev = new_node
        temp_node.next = new_node
        self.length += 1

    def pop_first(self):
        # Remove and return first node, or None if empty
        if not self.head:
            return None
        popped_node = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
            popped_node.next = None
        self.length -= 1
        return popped_node

    def pop(self):
        # Remove and return last node, or None if empty
        if not self.tail:
            return None
        popped_node = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            popped_node.prev = None
        self.length -= 1
        return popped_node

    def remove(self, index):
        # Remove and return node at index, or None if invalid
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()
        popped_node = self.get(index)
        popped_node.prev.next = popped_node.next
        popped_node.next.prev = popped_node.prev
        popped_node.prev = None
        popped_node.next = None
        self.length -= 1
        return popped_node

    def delete_all(self):
        # Clear entire list
        self.head = None
        self.tail = None
        self.length = 0


# Example usage
dll = DoublyLinkedList()
dll.prepend(5)
dll.prepend(44)
print(dll)  # Output: 44 <-> 5
