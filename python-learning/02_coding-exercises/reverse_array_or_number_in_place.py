# Question: Reverse an array/list without arr[::-1] or reversed(arr)
# Given an array/list, reverse its elements in place without using slicing or the built-in reversed() function.
# Example: [1, 2, 3, 4] → [4, 3, 2, 1]

"""
Approach:
Use two pointers: one starting at the beginning (left) and one at the end (right) of the array.
Swap the elements at these pointers, then move left pointer forward and right pointer backward.
Repeat until the pointers meet or cross.
This in-place reversal requires O(n/2) swaps and no extra space.

Time Complexity: O(n) where n is the length of the array
Space Complexity: O(1) as reversal is done in-place without extra storage
"""

def reverse_array(arr):
    left = 0
    right = len(arr) - 1

    while left < right:
        # Swap elements at left and right
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1

    return arr

# Test case
test_arr = [1, 2, 3, 4]
print("Reversed array:", reverse_array(test_arr))  # Output: [4, 3, 2, 1]



# Variation 1: Reverse digits in a number
"""
Note:
To reverse the digits of a number (e.g., 123456 → 654321), follow these steps:
1. Convert the number to a string and then to a list
2. Apply the same two-pointer logic
3. Join the result and convert back to integer
"""

def reverse_digits(num):
    num_list = list(str(num))
    left = 0
    right = len(num_list) - 1

    while left < right:
        num_list[left], num_list[right] = num_list[right], num_list[left]
        left += 1
        right -= 1

    return int(''.join(num_list))

# Test case
print("Reversed number:", reverse_digits(123456))  # Output: 654321



# Variation 2: Reverse a string using same logic
def reverse_string(s):
    char_list = list(s)
    left = 0
    right = len(char_list) - 1

    while left < right:
        char_list[left], char_list[right] = char_list[right], char_list[left]
        left += 1
        right -= 1

    return ''.join(char_list)

# Test case
print("Reversed string:", reverse_string("hello world"))  # Output: "dlrow olleh"



# Variation 3: Using built-in sort to reverse array (lexicographically)
"""
Note:
This uses in-built sort and reverse to reverse a list in descending order.
This is NOT the same as reversal of order — it's sorting in descending order.
"""

def reverse_with_sort(arr):
    arr.sort(reverse=True)
    return arr

# Test case
print("Sorted descending:", reverse_with_sort([4, 2, 7, 1]))  # Output: [7, 4, 2, 1]
