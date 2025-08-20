# Circular Queue implementation using a fixed-size list (array).
# Note: This code snippet is adapted from an online Udemy tutorial for learning purposes.

class Queue:
    """Circular Queue with fixed maximum size."""
    def __init__(self, maxSize):
        self.items = maxSize * [None]  # Fixed size list to hold queue elements
        self.maxSize = maxSize          # Maximum capacity of the queue
        self.start = -1                 # Points to the front element index
        self.top = -1                   # Points to the last element index
    
    def __str__(self):
        """Return string representation of the queue's current state."""
        values = [str(x) for x in self.items]
        return ' '.join(values)
    
    def isFull(self):
        """Check if the queue is full."""
        # Queue is full if top is just before start in a circular manner
        if self.top + 1 == self.start:
            return True
        elif self.start == 0 and self.top + 1 == self.maxSize:
            return True
        else:
            return False
    
    def isEmpty(self):
        """Check if the queue is empty."""
        return self.top == -1
    
    def enqueue(self, value):
        """Add an element to the end of the queue."""
        if self.isFull():
            return "The queue is full"
        else:
            # Circularly increment the top pointer
            if self.top + 1 == self.maxSize:
                self.top = 0
            else:
                self.top += 1
                if self.start == -1:  # If queue was empty, start points to first element
                    self.start = 0
            self.items[self.top] = value
            return "The element is inserted at the end of Queue"
    
    def dequeue(self):
        """Remove and return the front element from the queue."""
        if self.isEmpty():
            return "There is not any element in the Queue"
        else:
            firstElement = self.items[self.start]
            start = self.start
            # If queue had only one element, reset pointers
            if self.start == self.top:
                self.start = -1
                self.top = -1
            # Circularly increment the start pointer
            elif self.start + 1 == self.maxSize:
                self.start = 0
            else:
                self.start += 1
            self.items[start] = None
            return firstElement
    
    def peek(self):
        """Return the front element without removing it."""
        if self.isEmpty():
            return "There is not any element in the Queue"
        else:
            return self.items[self.start]
    
    def delete(self):
        """Reset the queue to empty state."""
        self.items = self.maxSize * [None]
        self.top = -1
        self.start = -1


# Example usage:
customQueue = Queue(3)
customQueue.enqueue(1)
customQueue.enqueue(2)
customQueue.enqueue(3)
customQueue.delete()
print(customQueue)  # Output will show empty queue as: None None None
