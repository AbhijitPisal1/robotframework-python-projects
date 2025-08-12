# Demonstrates how to use Python's built-in queue.Queue as a FIFO queue.
# Note: This code snippet is adapted from an online Udemy tutorial for learning purposes.

import queue as q

# Create a FIFO queue with max size 3
customQueue = q.Queue(maxsize=3)

print(customQueue.empty())  # Check if the queue is empty; prints True initially

# Add items to the queue
customQueue.put(1)
customQueue.put(2)
customQueue.put(3)

print(customQueue.full())   # Check if the queue is full; prints True

print(customQueue.get())    # Remove and print the first item (FIFO order), prints 1

print(customQueue.qsize())  # Print current size of the queue, prints 2
