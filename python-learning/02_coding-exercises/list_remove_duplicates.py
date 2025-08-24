# Question: Remove duplicates from list using set (but preserve order)
#
# Given a list of elements, remove duplicates while preserving
# the original order of the elements.
#
# Input: [1, 2, 2, 3, 1, 4]
# Output: [1, 2, 3, 4]

# -------------------------------------------------------
# Explanation of the Logic:
# 1. Initialize an empty dictionary to track which elements have been seen.
# 2. Initialize an empty list to store the result.
# 3. Iterate through the input list:
#    - For each element, check if it has been seen before.
#    - If not seen, append it to the result and mark it as seen.
# 4. This approach preserves the order of first occurrence
#    and removes all duplicates.
# -------------------------------------------------------

def remove_duplicates_preserve_order(lst):
    seen = {}
    result = []

    for item in lst:
        if item not in seen:
            result.append(item)
            seen[item] = True

    return result

# -------------------------------------------------------
# Time Complexity: O(n)
#   - n = length of the list
#   - One pass through the list, constant time membership checks
#
# Space Complexity: O(n)
#   - For the 'seen' dictionary and result list
# -------------------------------------------------------

# Test Case
test_list = [1, 2, 2, 3, 1, 4]
expected_output = [1, 2, 3, 4]

output = remove_duplicates_preserve_order(test_list)

print("Input List:       ", test_list)
print("Expected Output:  ", expected_output)
print("Actual Output:    ", output)
