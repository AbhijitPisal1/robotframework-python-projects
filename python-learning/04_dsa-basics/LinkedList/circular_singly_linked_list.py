"""
Circular Singly Linked List Implementation in Python

This file implements a circular singly linked list (CSLL) supporting creation,
insertion at different positions, traversal, searching, node deletion, and complete deletion.

Note: This code snippet is adapted from an online Udemy tutorial for educational purposes.

Classes:
- Node: Represents a single node with a value and a next pointer.
- CircularSinglyLinkedList: Manages the circular linked list structure and operations.

Key methods:
- createCSLL(value): Initializes the list with a single node that points to itself.
- insertCSLL(value, location): Inserts a node at the beginning (0), end (1), or given position.
- traversalCSLL(): Prints all nodes in the circular list once.
- searchCSLL(value): Searches for a node by value and returns it or a message if not found.
- deleteNode(location): Deletes node at beginning (0), end (1), or given position.
- deleteEntireCSLL(): Deletes the entire list safely.
"""

class Node:
    def __init__(self, value=None):
        self.value = value  # Data stored in node
        self.next = None    # Pointer to next node

class CircularSinglyLinkedList:
    def __init__(self):
        self.head = None  # Starting node of CSLL
        self.tail = None  # Last node (links back to head)

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
            if node == self.tail.next:
                break

    def createCSLL(self, nodeValue):
        # Create CSLL with single node pointing to itself
        node = Node(nodeValue)
        node.next = node
        self.head = node
        self.tail = node
        return "The CSLL has been created"

    def insertCSLL(self, value, location):
        # Insert new node at start (0), end (1), or specific position
        if self.head is None:
            return "The head reference is None"
        newNode = Node(value)
        if location == 0:
            newNode.next = self.head
            self.head = newNode
            self.tail.next = newNode
        elif location == 1:
            newNode.next = self.tail.next
            self.tail.next = newNode
            self.tail = newNode
        else:
            tempNode = self.head
            index = 0
            while index < location - 1:
                tempNode = tempNode.next
                index += 1
            newNode.next = tempNode.next
            tempNode.next = newNode
        return "The node has been successfully inserted"

    def traversalCSLL(self):
        # Print all nodes values once in circular list
        if self.head is None:
            print("There is not any element for traversal")
            return
        tempNode = self.head
        while True:
            print(tempNode.value)
            tempNode = tempNode.next
            if tempNode == self.tail.next:
                break

    def searchCSLL(self, nodeValue):
        # Search node by value, return node's value or message if not found
        if self.head is None:
            return "There is not any node in this CSLL"
        tempNode = self.head
        while True:
            if tempNode.value == nodeValue:
                return tempNode.value
            tempNode = tempNode.next
            if tempNode == self.tail.next:
                return "The node does not exist in this CSLL"

    def deleteNode(self, location):
        # Delete node at start (0), end (1), or specific position
        if self.head is None:
            print("There is not any node in CSLL")
            return
        if location == 0:
            if self.head == self.tail:
                self.head.next = None
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next
                self.tail.next = self.head
        elif location == 1:
            if self.head == self.tail:
                self.head.next = None
                self.head = None
                self.tail = None
            else:
                node = self.head
                while node.next != self.tail:
                    node = node.next
                node.next = self.head
                self.tail = node
        else:
            tempNode = self.head
            index = 0
            while index < location - 1:
                tempNode = tempNode.next
                index += 1
            nextNode = tempNode.next
            tempNode.next = nextNode.next

    def deleteEntireCSLL(self):
        # Delete entire list safely by breaking circular links
        self.head = None
        if self.tail:
            self.tail.next = None
        self.tail = None


# Example usage
circularSLL = CircularSinglyLinkedList()
circularSLL.createCSLL(0)
circularSLL.insertCSLL(1, 1)
circularSLL.insertCSLL(2, 1)
circularSLL.insertCSLL(3, 1)

print([node.value for node in circularSLL])  # Prints list values
circularSLL.deleteEntireCSLL()
print([node.value for node in circularSLL])  # Should print empty list
