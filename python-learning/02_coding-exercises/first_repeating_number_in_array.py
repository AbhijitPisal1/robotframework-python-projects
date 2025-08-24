# Question: First repeating number in a given array
# Given an array, find the first number that repeats (appears more than once).
# Example: [2, 5, 1, 2, 3, 5] → 2

"""
Approach:
Use a set to track seen numbers as we iterate through the array.
For each number, check if it has been seen before:
- If yes, this is the first repeating number, return it immediately.
- If no, add it to the set and continue.
If no repeating number is found, return None.
This method ensures the first repeating number in order is found in a single pass.
"""

def first_repeating_number(arr):
    seen = set()
    for num in arr:
        if num in seen:
            return num
        seen.add(num)
    return None  # If no repeating number found

# Time Complexity: O(n) where n is the length of the array
# Space Complexity: O(n) for the set storing seen elements

# Test case
test_arr = [2, 5, 1, 2, 3, 5]
print("Output:", first_repeating_number(test_arr))  # Output: 2


"""
Note:
If the input is a number like 47887654 and you want to find the first repeating digit, 
first convert the number to a string, then apply the same logic:
    for digit in str(num):
        if digit in seen:
            return digit
        seen.add(digit)
This treats digits like characters and works similarly to strings.
"""
