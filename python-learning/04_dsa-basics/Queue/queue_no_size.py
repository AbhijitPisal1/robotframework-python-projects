# Simple FIFO queue implementation using a Python list.
# Note: This code snippet is adapted from an online Udemy tutorial for learning purposes.

class Queue:
    """A basic FIFO queue implemented with a Python list."""
    
    def __init__(self):
        self.items = []  # List to store queue elements
    
    def __str__(self):
        """Return string representation of the queue items."""
        values = [str(x) for x in self.items]
        return ' '.join(values)
    
    def isEmpty(self):
        """Check if the queue is empty."""
        return self.items == []
    
    def enqueue(self, value):
        """Add an element at the end of the queue."""
        self.items.append(value)
        return "The element is inserted at the end of Queue"
    
    def dequeue(self):
        """Remove and return the element at the front of the queue.
        Returns a message if the queue is empty."""
        if self.isEmpty():
            return "There is not any element in the Queue"
        else:
            return self.items.pop(0)
    
    def peek(self):
        """Return the element at the front of the queue without removing it.
        Returns a message if the queue is empty."""
        if self.isEmpty():
            return "There is not any element in the Queue"
        else:
            return self.items[0]
    
    def delete(self):
        """Delete all elements in the queue."""
        self.items = None


# Example usage:
customQueue = Queue()
customQueue.enqueue(1)
customQueue.enqueue(2)
customQueue.enqueue(3)
print(customQueue.peek())  # Outputs: 1
customQueue.delete()
