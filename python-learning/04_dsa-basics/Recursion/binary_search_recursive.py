# Binary Search of a value in a sorted array using recursion

def binarySearchRecursive(array, value, start, end):
    if start > end:
        return -1  # Base case: value not found in the array segment

    middle = (start + end) // 2

    if array[middle] == value:
        return middle  # Value found at the middle index
    elif value < array[middle]:
        # Search in the left half
        return binarySearchRecursive(array, value, start, middle - 1)
    else:
        # Search in the right half
        return binarySearchRecursive(array, value, middle + 1, end)

# Usage example:
custArray = [2, 5, 8, 12, 16, 23, 38]
print(binarySearchRecursive(custArray, 16, 0, len(custArray) - 1))  # Output: 4

"""
Output Explanation for binarySearchRecursive(custArray, 16, 0, 6)
→ middle index = 3, value at index 3 is 12, 16 > 12
→ Search in right half: start=4, end=6
→ middle index = 5, value at index 5 is 23, 16 < 23
→ Search in left half: start=4, end=4
→ middle index = 4, value at index 4 is 16, found at index 4
"""
