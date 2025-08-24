# Question: Find unique elements between two lists (symmetric difference)
#
# Given two lists of integers, return a new list containing elements
# that appear in only one of the lists (i.e., not in both).
#
# Input: [1, 2, 3], [2, 3, 4]
# Output: [1, 4]

# -------------------------------------------------------
# Explanation of the Logic:
# 1. Create two frequency dictionaries (or hash maps) to track the presence of elements in each list.
# 2. Iterate through the first list and mark each element as present.
# 3. Do the same for the second list.
# 4. Then, go through both lists again:
#    - Add elements from list1 that are NOT in list2.
#    - Add elements from list2 that are NOT in list1.
# This ensures we collect only the unique (non-overlapping) elements.
# -------------------------------------------------------

def symmetric_difference(list1, list2):
    # Build presence tracking for each list
    in_list1 = {}
    in_list2 = {}

    for item in list1:
        in_list1[item] = True

    for item in list2:
        in_list2[item] = True

    result = []

    # Add items that are in list1 but not in list2
    for item in list1:
        if item not in in_list2:
            result.append(item)

    # Add items that are in list2 but not in list1
    for item in list2:
        if item not in in_list1:
            result.append(item)

    return result

# -------------------------------------------------------
# Time Complexity: O(n + m)
#   - n = len(list1), m = len(list2)
#   - One pass to build presence dictionaries
#   - One pass to build result
#
# Space Complexity: O(n + m)
#   - To store element presence from both lists
# -------------------------------------------------------

# Test Case
list1 = [1, 2, 3]
list2 = [2, 3, 4]
expected_output = [1, 4]

output = symmetric_difference(list1, list2)

print("Input List 1:      ", list1)
print("Input List 2:      ", list2)
print("Expected Output:   ", expected_output)
print("Actual Output:     ", output)
