# multistack_fixed_array.py
# Implementation of three separate stacks using a single fixed-size array.
# Note: This code snippet is adapted from an online Udemy tutorial for learning purposes.

class MultiStack:
    """Implements three stacks using a single list (array) with fixed size per stack."""
    
    def __init__(self, stacksize):
        self.numstacks = 3
        self.stacksize = stacksize
        self.array = [0] * (stacksize * self.numstacks)  # Combined array for all stacks
        self.sizes = [0] * self.numstacks  # Tracks current size of each stack

    def Push(self, item, stacknum):
        """Push an item onto the specified stack (0, 1, or 2)."""
        if self.IsFull(stacknum):
            raise Exception('Stack is full')
        self.sizes[stacknum] += 1
        self.array[self.IndexOfTop(stacknum)] = item

    def Pop(self, stacknum):
        """Pop the top item from the specified stack."""
        if self.IsEmpty(stacknum):
            raise Exception('Stack is empty')
        top_index = self.IndexOfTop(stacknum)
        value = self.array[top_index]
        self.array[top_index] = 0  # Optional: Reset to 0 for clarity
        self.sizes[stacknum] -= 1
        return value

    def Peek(self, stacknum):
        """Return the top item of the specified stack without removing it."""
        if self.IsEmpty(stacknum):
            raise Exception('Stack is empty')
        return self.array[self.IndexOfTop(stacknum)]

    def IsEmpty(self, stacknum):
        """Check if the specified stack is empty."""
        return self.sizes[stacknum] == 0

    def IsFull(self, stacknum):
        """Check if the specified stack is full."""
        return self.sizes[stacknum] == self.stacksize

    def IndexOfTop(self, stacknum):
        """Calculate the index of the top item of the specified stack in the array."""
        offset = stacknum * self.stacksize
        return offset + self.sizes[stacknum] - 1


# Example usage:
stack = MultiStack(1)
stack.Push(10, 0)
stack.Push(20, 1)
stack.Push(30, 2)
print(stack.Peek(0))  # Output: 10
print(stack.Peek(1))  # Output: 20
print(stack.Peek(2))  # Output: 30
