# Problem: Check if a list is a palindrome
# Given a list, determine if it reads the same forwards and backwards.
# Input example: [1, 2, 3, 2, 1]
# Output: True

"""
Approach:
Use two pointers: one starting at the beginning (left) and one at the end (right) of the list.
Compare the elements at these pointers.
If at any point they differ, the list is not a palindrome.
Move the pointers towards each other until they meet or cross.
If all matched, return True.
"""

def is_palindrome(lst):
    left = 0
    right = len(lst) - 1

    while left < right:
        if lst[left] != lst[right]:
            return False
        left += 1
        right -= 1

    return True

"""
Note:
- For strings, this palindrome check works directly since strings are iterable like lists.
- For numbers, convert the number to a string first (e.g., str(num)) to treat digits as characters,
  then apply the same palindrome logic.
- No change in the palindrome-checking logic is needed; only the input type adapts.
"""

# Time Complexity: O(n) where n is the length of the list
# Space Complexity: O(1) since only two pointers are used

# Test case
test_list = [1, 2, 3, 2, 1]
print("Output:", is_palindrome(test_list))  # Output: True
