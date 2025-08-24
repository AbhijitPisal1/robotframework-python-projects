# Question: Classify values in an array as greater than, less than, or equal to the middle index value
# Given an array, return three lists containing elements that are greater than,
# less than, and equal to the element at the middle index.
# Example: arr = [10, 20, 30, 40, 50, 30, 10, 60]
# Output:
# Greater than middle: [40, 50, 60]
# Less than middle: [10, 20, 10]
# Equal to middle: [30, 30]

"""
Approach:
- Find the middle index of the array using integer division: mid_index = len(arr) // 2
- Retrieve the middle value from the array.
- Initialize three separate lists to store elements greater than, less than, and equal to the middle value.
- Iterate through the array once:
    - Append elements to the corresponding list based on comparison with the middle value.
- Return all three lists.

This approach uses a single pass through the array, making it efficient.

Use cases:
- Useful in data analysis where relative positioning to a central reference value is needed.
- Helpful in partitioning data based on a pivot or median-like element.
- Can assist in algorithms that require classification of values relative to a middle or median element.

Time Complexity: O(n) where n is the length of the array
Space Complexity: O(n) in the worst case (when all elements fall into one category)
"""

def values_compare_to_middle(arr):
    if len(arr) == 0:
        return [], [], []  # Return three empty lists for empty input

    mid_index = len(arr) // 2
    mid_value = arr[mid_index]

    greater = []
    lesser = []
    equal = []

    for value in arr:
        if value > mid_value:
            greater.append(value)
        elif value < mid_value:
            lesser.append(value)
        else:
            equal.append(value)

    return greater, lesser, equal

# Test case
test_arr = [10, 20, 30, 40, 50, 30, 10, 60]
greater, lesser, equal = values_compare_to_middle(test_arr)
print("Greater than middle:", greater)  # Output: [40, 50, 60]
print("Less than middle:", lesser)      # Output: [10, 20, 10]
print("Equal to middle:", equal)        # Output: [30, 30]
