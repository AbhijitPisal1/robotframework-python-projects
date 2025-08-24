# Question: Flatten a nested list
# Given a list of lists, flatten it into a single list containing all the elements in order.
# Input: [[1, 2], [3, 4], [5]]
# Output: [1, 2, 3, 4, 5]

"""
Approach:
Iterate through each sublist in the nested list.
For each sublist, iterate through its elements and append them to a result list.
This simple nested loop approach ensures all elements are collected in order.
"""

def flatten_nested_list(nested_list):
    flattened = []
    for sublist in nested_list:
        for item in sublist:
            flattened.append(item)
    return flattened

# Time Complexity: O(n) where n is the total number of elements in all sublists
# Space Complexity: O(n) for the output list storing all elements

# Test case
test_input = [[1, 2], [3, 4], [5]]
print("Output:", flatten_nested_list(test_input))  # Output: [1, 2, 3, 4, 5]