# Implementation of a basic FIFO Queue using a singly linked list.
# Note: This code snippet is adapted from an online Udemy tutorial for learning purposes.

class Node:
    """Node class represents an element in the linked list."""
    def __init__(self, value=None):
        self.value = value  # Node data
        self.next = None    # Pointer to the next node
    
    def __str__(self):
        return str(self.value)

class LinkedList:
    """Singly linked list supporting iteration."""
    def __init__(self):
        self.head = None  # Start of the list
        self.tail = None  # End of the list
    
    def __iter__(self):
        """Allows iteration over nodes in the linked list."""
        curNode = self.head
        while curNode:
            yield curNode
            curNode = curNode.next

class Queue:
    """FIFO queue implemented using a linked list."""
    def __init__(self):
        self.linkedList = LinkedList()
    
    def __str__(self):
        """Return string of all queue elements in order."""
        values = [str(x) for x in self.linkedList]
        return ' '.join(values)
    
    def enqueue(self, value):
        """Add an item to the end of the queue."""
        newNode = Node(value)
        if self.linkedList.head is None:
            self.linkedList.head = newNode
            self.linkedList.tail = newNode
        else:
            self.linkedList.tail.next = newNode
            self.linkedList.tail = newNode
    
    def isEmpty(self):
        """Check if the queue is empty."""
        return self.linkedList.head is None
    
    def dequeue(self):
        """Remove and return the item at the front of the queue.
        Returns a message if the queue is empty."""
        if self.isEmpty():
            return "There is not any node in the Queue"
        else:
            tempNode = self.linkedList.head
            if self.linkedList.head == self.linkedList.tail:
                # Only one node in queue
                self.linkedList.head = None
                self.linkedList.tail = None
            else:
                self.linkedList.head = self.linkedList.head.next
            return tempNode
    
    def peek(self):
        """Return the item at the front of the queue without removing it."""
        if self.isEmpty():
            return "There is not any node in the Queue"
        else:
            return self.linkedList.head
    
    def delete(self):
        """Delete all items from the queue."""
        self.linkedList.head = None
        self.linkedList.tail = None


# Example usage:
custQueue = Queue()
custQueue.enqueue(1)
custQueue.enqueue(2)
custQueue.enqueue(3)
print(custQueue)       # Output: 1 2 3
print(custQueue.peek())  # Output: 1 (node at front)
print(custQueue)       # Output still: 1 2 3 (peek does not remove)
