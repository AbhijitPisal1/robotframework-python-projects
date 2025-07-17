# Question: Find duplicates in an array using HashSet for O(n) time complexity.

def find_duplicates(nums):
    """Find duplicates in an array using a HashSet."""
    seen = set()  # HashSet to keep track of seen numbers
    duplicates = []  # List to hold duplicate numbers

    for num in nums:
        if num in seen:
            duplicates.append(num)  # If the number is already seen, it's a duplicate
        else:
            seen.add(num)  # Add the number to the HashSet

    return duplicates


# Example usage:
input_array = [1, 2, 3, 4, 2, 3, 5]
result = find_duplicates(input_array)
print(f"The duplicates in the array are: {result}")  # Output: The duplicates in the array are: [2, 3].

""" Alternate way Find duplicates in an array using Counter from collections

python
from collections import Counter

def find_duplicates(nums):
    count = Counter(nums)  # Count occurrences of each number
    duplicates = [num for num, freq in count.items() if freq > 1]  # Extract duplicates

    return duplicates

# Example usage:
input_array = [1, 2, 3, 4, 2, 3, 5]
result = find_duplicates(input_array)
print(f"The duplicates in the array are: {result}")  # Output: The duplicates in the array are: [2, 3].
"""
