# Demonstrates how to use multiprocessing.Queue as a FIFO queue.
# Note: This code snippet is adapted from an online Udemy tutorial for learning purposes.

from multiprocessing import Queue

# Create a FIFO queue with max size 3 (maxsize is optional)
customQueue = Queue(maxsize=3)

customQueue.put(1)       # Add item to the queue
print(customQueue.get()) # Remove and print the first item (FIFO order)
