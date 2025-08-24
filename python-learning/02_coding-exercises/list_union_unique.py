# Question: Find union of two lists without duplicates
#
# Given two lists of integers, return a new list containing all unique elements
# from both lists combined. The result should preserve the order in which
# elements first appear across both lists.
#
# Input: [1, 2], [2, 3]
# Output: [1, 2, 3]

# -------------------------------------------------------
# Explanation of the Logic:
# 1. Initialize an empty dictionary (used as a hash map) to track seen elements.
# 2. Initialize an empty result list.
# 3. Iterate through the first list:
#    - If the element is not in the seen dictionary, add it to the result and mark it seen.
# 4. Repeat the same for the second list.
# This ensures all elements are added in the order they appear, and only once.
# -------------------------------------------------------

def union_unique(list1, list2):
    seen = {}
    result = []

    # Add elements from the first list
    for item in list1:
        if item not in seen:
            result.append(item)
            seen[item] = True

    # Add elements from the second list
    for item in list2:
        if item not in seen:
            result.append(item)
            seen[item] = True

    return result

# -------------------------------------------------------
# Time Complexity: O(n + m)
#   - n = len(list1), m = len(list2)
#   - Each list is traversed once
#
# Space Complexity: O(n + m)
#   - For storing unique elements in a dictionary and result list
# -------------------------------------------------------

# Test Case
list1 = [1, 2]
list2 = [2, 3]
expected_output = [1, 2, 3]

output = union_unique(list1, list2)

print("Input List 1:     ", list1)
print("Input List 2:     ", list2)
print("Expected Output:  ", expected_output)
print("Actual Output:    ", output)
