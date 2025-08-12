# Implementation of a Circular Singly Linked List (CSLL) with basic operations:
# append, prepend, insert, traverse, search, get, set, pop, remove, and delete all.
# Note: This code snippet is adapted from an online Udemy tutorial for learning purposes.

class Node:
    """A node in a circular singly linked list."""
    def __init__(self, value):
        self.value = value  # Node's data
        self.next = None    # Pointer to the next node
    
    def __str__(self):
        return str(self.value)  # String representation of the node's value

class CSLinkedList:
    """Circular Singly Linked List implementation."""

    def __init__(self):
        self.head = None  # First node
        self.tail = None  # Last node
        self.length = 0   # Number of nodes in the list
    
    def __str__(self):
        """Return a string showing the list values in order."""
        temp_node = self.head
        result = ''
        while temp_node is not None:
            result += str(temp_node.value)
            temp_node = temp_node.next
            if temp_node == self.head:  # Stop after completing one full circle
                break
            result += ' -> '
        return result
    
    def append(self, value):
        """Add a node to the end of the list."""
        new_node = Node(value)
        if self.length == 0:  # If list is empty
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node  # Points to itself, circular link
        else:
            self.tail.next = new_node  # Old tail points to new node
            new_node.next = self.head  # New node points to head to maintain circularity
            self.tail = new_node       # Update tail to new node
        self.length += 1
    
    def prepend(self, value):
        """Add a node at the beginning of the list."""
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
        else:
            new_node.next = self.head
            self.head = new_node
            self.tail.next = new_node  # Tail must point to new head to keep list circular
        self.length += 1
    
    def insert(self, index, value):
        """Insert a node at a specified index."""
        if index < 0 or index > self.length:
            raise Exception("Index out of range")
        
        new_node = Node(value)
        if index == 0:
            if self.length == 0:
                self.head = new_node
                self.tail = new_node
                new_node.next = new_node
            else:
                new_node.next = self.head
                self.head = new_node
                self.tail.next = new_node  # Maintain circularity
        elif index == self.length:
            self.tail.next = new_node
            new_node.next = self.head
            self.tail = new_node
        else:
            temp_node = self.head
            for _ in range(index - 1):
                temp_node = temp_node.next
            new_node.next = temp_node.next
            temp_node.next = new_node
        self.length += 1
    
    def traverse(self):
        """Print all node values in the list."""
        if not self.head:
            return
        current = self.head
        while True:
            print(current.value)
            current = current.next
            if current == self.head:
                break
    
    def search(self, target):
        """
        Search for a node by value.
        Returns the index if found, else -1.
        """
        current = self.head
        index = 0
        while current is not None:
            if current.value == target:
                return index
            current = current.next
            index += 1
            if current == self.head:
                break
        return -1
    
    def get(self, index):
        """
        Get the node at a specific index.
        Supports index = -1 to get the tail node.
        Returns None if index invalid.
        """
        if index == -1:
            return self.tail
        if index < -1 or index >= self.length:
            return None
        current = self.head
        for _ in range(index):
            current = current.next
        return current
    
    def set_value(self, index, value):
        """Set the value of the node at the given index."""
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False
    
    def pop_first(self):
        """Remove and return the first node in the list."""
        if self.length == 0:
            return None
        popped_node = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.tail.next = self.head  # Maintain circular link
            popped_node.next = None     # Disconnect popped node
        self.length -= 1
        return popped_node
    
    def pop(self):
        """Remove and return the last node in the list."""
        if self.length == 0:
            return None
        popped_node = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            temp = self.head
            while temp.next != self.tail:  # Find second last node
                temp = temp.next
            temp.next = self.head  # Close the circular link
            self.tail = temp       # Update tail
        popped_node.next = None
        self.length -= 1
        return popped_node
    
    def remove(self, index):
        """
        Remove node at a given index.
        Supports -1 to remove last node.
        Returns the removed node or None if index invalid.
        """
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
    
    def delete_all(self):
        """Delete the entire list."""
        if self.length == 0:
            return
        self.tail.next = None  # Break circular link to help garbage collection
        self.head = None
        self.tail = None
        self.length = 0


# Example usage
linked_list = CSLinkedList()
print(linked_list)  # Should print empty string
linked_list.append(10)
linked_list.insert(0, 20)
linked_list.insert(1, 30)
linked_list.insert(2, 40)
linked_list.insert(3, 50)
print(linked_list)  # Print list after insertions
print(linked_list.set_value(-1, 100))  # Update tail value to 100
print(linked_list)  # Print list after update
