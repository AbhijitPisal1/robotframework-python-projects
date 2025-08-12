"""
LinkedList Implementation in Python

This file contains a basic singly linked list data structure with essential methods such as
append, prepend, insert, remove, search, and traversal. It is designed for beginners to
understand how linked lists work internally.

Note: This code snippet is adapted from an online Udemy tutorial for educational purposes.

Classes:
- Node: Represents an individual node in the linked list.
- LinkedList: Manages the linked list operations.

Key methods:
- append(value): Adds a new node with the given value at the end.
- prepend(value): Adds a new node at the beginning.
- insert(index, value): Inserts a new node at the specified index.
- remove(index): Removes the node at the given index.
- search(target): Returns the index of the node containing the target value or -1 if not found.
- get(index): Retrieves the node at the specified index.
- set_value(index, value): Updates the value of the node at the index.
- pop(): Removes and returns the last node.
- pop_first(): Removes and returns the first node.
- traverse(): Prints all node values in order.
"""

class Node:
    def __init__(self, value):
        self.value = value  # Store the data
        self.next = None    # Pointer to the next node (default None)

class LinkedList:
    def __init__(self):
        self.head = None   # Start of the list
        self.tail = None   # End of the list
        self.length = 0    # Number of nodes
    
    def __str__(self):
        # Return string representation like "10 -> 20 -> 30"
        temp_node = self.head
        result = ''
        while temp_node is not None:
            result += str(temp_node.value)
            if temp_node.next is not None:
                result += ' -> '
            temp_node = temp_node.next
        return result
    
    def append(self, value):
        # Add node at end
        new_node = Node(value)
        if self.head is None:  # Empty list
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
    
    def prepend(self, value):
        # Add node at start
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
    
    def insert(self, index, value):
        # Insert node at given index
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        elif index == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            temp_node = self.head
            for _ in range(index-1):
                temp_node = temp_node.next
            new_node.next = temp_node.next
            temp_node.next = new_node
        self.length += 1
    
    def traverse(self):
        # Print all node values
        current = self.head
        while current is not None:
            print(current.value)
            current = current.next
    
    def search(self, target):
        # Return index of target value, else -1
        current = self.head
        index = 0
        while current is not None:
            if current.value == target:
                return index
            current = current.next
            index += 1
        return -1
    
    def get(self, index):
        # Return node at index (-1 for tail), else None
        if index == -1:
            return self.tail
        elif index < -1 or index >= self.length:
            return None
        current = self.head
        for _ in range(index):
            current = current.next
        return current
    
    def set_value(self, index, value):
        # Update value of node at index
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False
    
    def pop_first(self):
        # Remove and return first node
        if self.length == 0:
            return None
        popped_node = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            popped_node.next = None
        self.length -= 1
        return popped_node
    
    def pop(self):
        # Remove and return last node
        if self.length == 0:
            return None
        popped_node = self.tail
        if self.length == 1:
            self.head = self.tail = None
        else:
            temp = self.head
            while temp.next is not self.tail:
                temp = temp.next
            temp.next = None
            self.tail = temp
        self.length -= 1
        return popped_node
    
    def remove(self, index):
        # Remove node at index and return it
        if index < -1 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == -1 or index == self.length - 1:
            return self.pop()
        prev_node = self.get(index - 1)
        popped_node = prev_node.next
        prev_node.next = popped_node.next
        popped_node.next = None
        self.length -= 1
        return popped_node


# Example usage
linked_list = LinkedList()
linked_list.append(10)
linked_list.append(20)
linked_list.append(30)
linked_list.append(40)
print(linked_list)          # Output: 10 -> 20 -> 30 -> 40
print(linked_list.remove(0))  # Removes first node (10)
print(linked_list)          # Output: 20 -> 30 -> 40
