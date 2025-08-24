# Question: Check if two lists are equal (unordered, duplicates not allowed)
# Given two lists, determine if they contain the same unique elements regardless of order.
# Duplicates should be ignored.
# Example: [1, 2, 2, 3] and [3, 2, 1, 1] → True (unique sets are {1,2,3} for both)
#          [1, 2, 3] and [3, 2, 4] → False

"""
Approach:
Convert both lists to sets to ignore duplicates and capture unique elements.
Compare the two sets for equality.
If equal, return True, else False.
"""

def are_lists_equal_unordered_no_duplicates(list1, list2):
    set1 = set()
    for item in list1:
        set1.add(item)
    set2 = set()
    for item in list2:
        set2.add(item)
    return set1 == set2

# Time Complexity: O(n + m) where n and m are the lengths of the two lists
# Space Complexity: O(k) where k is the number of unique elements in the lists

# Test case
list_a = [1, 2, 2, 3]
list_b = [3, 2, 1, 1]
print("Output:", are_lists_equal_unordered_no_duplicates(list_a, list_b))  # Output: True