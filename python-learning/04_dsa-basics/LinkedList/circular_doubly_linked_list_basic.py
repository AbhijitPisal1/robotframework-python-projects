# This code implements a Circular Doubly Linked List (CDLL) with basic operations
# such as creation, insertion, traversal, reverse traversal, searching, and deletion.
# Note: This code snippet is adapted from an online Udemy tutorial for learning purposes.

class Node:
    """A Node in a circular doubly linked list."""
    def __init__(self, value=None):
        self.value = value  # The data value of the node
        self.next = None    # Pointer to the next node in the list
        self.prev = None    # Pointer to the previous node in the list

class CircularDoublyLinkedList:
    """Implementation of a Circular Doubly Linked List (CDLL)."""

    def __init__(self):
        self.head = None  # Start of the list
        self.tail = None  # End of the list

    def __iter__(self):
        """Allows iteration over the CDLL nodes using a for-loop or list comprehension."""
        node = self.head
        while node:
            yield node
            node = node.next
            if node == self.tail.next:  # Stop once we've looped back to the head
                break

    def createCDLL(self, nodeValue):
        """Create a CDLL with a single node."""
        newNode = Node(nodeValue)
        self.head = newNode
        self.tail = newNode
        newNode.prev = newNode  # Circular link to itself
        newNode.next = newNode  # Circular link to itself
        return "The CDLL is created successfully"

    def insertCDLL(self, value, location):
        """
        Insert a node into the CDLL at a specified location.
        location = 0 for beginning, 1 for end, and any other number for specific index.
        """
        if self.head is None:
            return "The CDLL does not exist"
        newNode = Node(value)
        if location == 0:  # Insert at beginning
            newNode.next = self.head
            newNode.prev = self.tail
            self.head.prev = newNode
            self.tail.next = newNode
            self.head = newNode
        elif location == 1:  # Insert at end
            newNode.next = self.head
            newNode.prev = self.tail
            self.tail.next = newNode
            self.head.prev = newNode
            self.tail = newNode
        else:  # Insert at a specific middle location
            tempNode = self.head
            index = 0
            while index < location - 1:
                tempNode = tempNode.next
                index += 1
            newNode.next = tempNode.next
            newNode.prev = tempNode
            tempNode.next.prev = newNode
            tempNode.next = newNode
        return "The node has been successfully inserted"

    def traversalCDLL(self):
        """Traverse the CDLL from head to tail and print node values."""
        if self.head is None:
            print("There is not any node for traversal")
            return
        tempNode = self.head
        while True:
            print(tempNode.value)
            if tempNode == self.tail:
                break
            tempNode = tempNode.next

    def reverseTraversalCDLL(self):
        """Traverse the CDLL from tail to head and print node values."""
        if self.head is None:
            print("There is not any node for reverse traversal")
            return
        tempNode = self.tail
        while True:
            print(tempNode.value)
            if tempNode == self.head:
                break
            tempNode = tempNode.prev

    def searchCDLL(self, nodeValue):
        """Search for a node by its value in the CDLL."""
        if self.head is None:
            return "There is not any node in CDLL"
        tempNode = self.head
        while True:
            if tempNode.value == nodeValue:
                return tempNode.value
            if tempNode == self.tail:
                break
            tempNode = tempNode.next
        return "The value does not exist in CDLL"

    def deleteNode(self, location):
        """
        Delete a node from the CDLL.
        location = 0 for head, 1 for tail, any other number for a specific index.
        """
        if self.head is None:
            print("There is not any node to delete")
            return
        if self.head == self.tail:  # Only one node in the list
            self.head.prev = None
            self.head.next = None
            self.head = None
            self.tail = None
            print("The node has been successfully deleted")
            return

        if location == 0:  # Delete head node
            self.head = self.head.next
            self.head.prev = self.tail
            self.tail.next = self.head
        elif location == 1:  # Delete tail node
            self.tail = self.tail.prev
            self.tail.next = self.head
            self.head.prev = self.tail
        else:  # Delete node at specific location
            curNode = self.head
            index = 0
            while index < location - 1:
                curNode = curNode.next
                index += 1
            curNode.next = curNode.next.next
            curNode.next.prev = curNode
        print("The node has been successfully deleted")

    def deleteCDLL(self):
        """Delete the entire Circular Doubly Linked List."""
        if self.head is None:
            print("There is not any element to delete")
            return
        self.tail.next = None  # Break the circular reference to help garbage collection
        tempNode = self.head
        while tempNode:
            tempNode.prev = None
            tempNode = tempNode.next
        self.head = None
        self.tail = None
        print("The CDLL has been successfully deleted")


# Example usage:
circularDLL = CircularDoublyLinkedList()
circularDLL.createCDLL(5)
circularDLL.insertCDLL(0, 0)  # Insert at beginning
circularDLL.insertCDLL(1, 1)  # Insert at end
circularDLL.insertCDLL(2, 2)  # Insert at position 2
print([node.value for node in circularDLL])  # Display values in CDLL
circularDLL.deleteCDLL()
print([node.value for node in circularDLL])  # Should be empty now
