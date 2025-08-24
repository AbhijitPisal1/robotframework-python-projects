# Question: Longest string in a given list without using max(lst, key=len)
# Given a list of strings, return the longest string without using the built-in max() function with key=len.
# Input example: ["apple", "banana", "cherry", "date"]
# Output: "banana"

"""
Approach:
Initialize a variable to hold the longest string, starting with the first string in the list.
Iterate through each string in the list, compare its length with the length of the current longest string.
If the current string is longer, update the longest string variable.
After checking all strings, the variable contains the longest string.
This requires a single pass through the list.

Time Complexity: O(n) where n is the number of strings in the list
Space Complexity: O(1) since only one variable tracks the longest string
"""

def find_longest_string(strings):
    if len(strings) == 0:
        raise ValueError("List cannot be empty")

    longest = strings[0]
    for s in strings:
        if len(s) > len(longest):
            longest = s
    return longest

"""
Note:
To find the shortest string instead, simply change the comparison operator in the if condition:
    if len(s) < len(shortest):
        shortest = s
and initialize a variable named 'shortest' instead of 'longest'.
See the next function for a full example.
"""

# Test case
test_strings = ["apple", "banana", "cherry", "date"]
print("Output:", find_longest_string(test_strings))  # Output: "banana"
