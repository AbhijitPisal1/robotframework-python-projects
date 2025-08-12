"""
Doubly Linked List Implementation in Python

This file implements a basic doubly linked list (DLL) with common operations such as
creation, insertion, traversal (forward and reverse), searching, node deletion, and
complete list deletion.

Note: This code snippet is adapted from an online Udemy tutorial for educational purposes.

Classes:
- Node: Represents a node with pointers to both next and previous nodes.
- DoublyLinkedList: Manages the DLL operations.

Key methods:
- createDLL(value): Initializes the doubly linked list with a single node.
- insertNode(value, location): Inserts a new node at the start (0), end (1), or specific index.
- traverseDLL(): Prints all node values from head to tail.
- reverseTraversalDLL(): Prints all node values from tail to head.
- searchDLL(value): Returns the node’s value if found, else indicates absence.
- deleteNode(location): Deletes node at start (0), end (1), or a specific index.
- deleteDLL(): Deletes the entire doubly linked list.
"""

class Node:
    def __init__(self, value=None):
        self.value = value    # Data stored in the node
        self.next = None      # Pointer to next node
        self.prev = None      # Pointer to previous node

class DoublyLinkedList:
    def __init__(self):
        self.head = None      # Start of the DLL
        self.tail = None      # End of the DLL
    
    def __iter__(self):
        # Allows iteration over the DLL nodes (e.g. for node in dll)
        node = self.head
        while node:
            yield node
            node = node.next
    
    def createDLL(self, nodeValue):
        # Create DLL with a single node
        node = Node(nodeValue)
        node.prev = None
        node.next = None
        self.head = node
        self.tail = node
        return "The DLL is created Successfully"
    
    def insertNode(self, nodeValue, location):
        # Insert node at beginning (0), end (1), or specific index (>1)
        if self.head is None:
            print("The node cannot be inserted")
        else:
            newNode = Node(nodeValue)
            if location == 0:
                # Insert at beginning
                newNode.prev = None
                newNode.next = self.head
                self.head.prev = newNode
                self.head = newNode
            elif location == 1:
                # Insert at end
                newNode.next = None
                newNode.prev = self.tail
                self.tail.next = newNode
                self.tail = newNode
            else:
                # Insert at given index
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                newNode.next = tempNode.next
                newNode.prev = tempNode
                newNode.next.prev = newNode
                tempNode.next = newNode
    
    def traverseDLL(self):
        # Print all values from head to tail
        if self.head is None:
            print("There is not any element to traverse")
        else:
            tempNode = self.head
            while tempNode:
                print(tempNode.value)
                tempNode = tempNode.next
    
    def reverseTraversalDLL(self):
        # Print all values from tail to head
        if self.head is None:
            print("There is not any element to traverse")
        else:
            tempNode = self.tail
            while tempNode:
                print(tempNode.value)
                tempNode = tempNode.prev
    
    def searchDLL(self, nodeValue):
        # Search for node by value, return value or not found message
        if self.head is None:
            return "There is not any element in the list"
        else:
            tempNode = self.head
            while tempNode:
                if tempNode.value == nodeValue:
                    return tempNode.value
                tempNode = tempNode.next
            return "The node does not exist in this list"
    
    def deleteNode(self, location):
        # Delete node at beginning (0), end (1), or specific index (>1)
        if self.head is None:
            print("There is not any element in DLL")
        else:
            if location == 0:
                # Delete first node
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
                    self.head.prev = None
            elif location == 1:
                # Delete last node
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.tail = self.tail.prev
                    self.tail.next = None
            else:
                # Delete node at index
                curNode = self.head
                index = 0
                while index < location - 1:
                    curNode = curNode.next
                    index += 1
                curNode.next = curNode.next.next
                curNode.next.prev = curNode
            print("The node has been successfully deleted")
    
    def deleteDLL(self):
        # Delete the entire DLL
        if self.head is None:
            print("There is not any node in DLL")
        else:
            tempNode = self.head
            while tempNode:
                tempNode.prev = None
                tempNode = tempNode.next
            self.head = None
            self.tail = None
            print("The DLL has been successfully deleted")


# Example usage
doubyLL = DoublyLinkedList()
doubyLL.createDLL(5)
doubyLL.insertNode(0, 0)   # Insert at beginning
doubyLL.insertNode(2, 1)   # Insert at end
doubyLL.insertNode(6, 2)   # Insert at index 2
print([node.value for node in doubyLL])  # Output: [0, 5, 6, 2]
doubyLL.deleteDLL()
print([node.value for node in doubyLL])  # Output: []
