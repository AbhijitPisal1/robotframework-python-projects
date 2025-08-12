# Example showing how to use collections.deque as a FIFO queue with a fixed size.
# Note: This code snippet is adapted from an online Udemy tutorial for learning purposes.

from collections import deque

# Create a deque with max length 3 - acts like a fixed-size FIFO queue
customQueue = deque(maxlen=3)
print(customQueue)  # Outputs: deque([]), empty queue initially

# Append items; when maxlen is reached, oldest items are discarded automatically
customQueue.append(1)
customQueue.append(2)
customQueue.append(3)
customQueue.append(4)  # '1' will be removed, queue now holds 2,3,4
print(customQueue)    # Outputs: deque([2, 3, 4], maxlen=3)

customQueue.clear()   # Clear all items from the queue
print(customQueue)    # Outputs: deque([]), empty queue again
