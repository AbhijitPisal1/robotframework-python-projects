"""
Problem:
1. Sort a list of names alphabetically (lexicographically).
2. Sort a list of names based on the length of each name in ascending order.

Approach:
Both use Insertion Sort to demonstrate sorting logic explicitly without using Python's built-in sorted().
- For alphabetical sort, strings are compared lexicographically.
- For length-based sort, comparison is based on the length of each string.

Time Complexity: O(n^2) for both (due to insertion sort)
Space Complexity: O(1) since sorting is done in-place
"""

def alphabetical_sort(names):
    """
    Sorts a list of strings alphabetically (lexicographically) in ascending order using insertion sort.
    """
    n = len(names)
    for i in range(1, n):
        key = names[i]
        j = i - 1
        # Shift elements that are greater lex order than key one step ahead
        while j >= 0 and names[j] > key:
            names[j + 1] = names[j]
            j -= 1
        names[j + 1] = key
    return names

"""
Note on Descending Order:
To sort in descending order instead of ascending,
simply reverse the comparison operators in the while loop:
    change names[j] > key to names[j] < key
"""
def sort_names_by_length(names):
    """
    Sorts a list of strings by the length of each string in ascending order using insertion sort.
    """
    n = len(names)
    for i in range(1, n):
        key = names[i]
        key_length = len(key)
        j = i - 1
        # Shift elements with length greater than key_length one step ahead
        while j >= 0 and len(names[j]) > key_length:
            names[j + 1] = names[j]
            j -= 1
        names[j + 1] = key
    return names

"""
Note on Descending Order:
To sort in descending order instead of ascending,
simply reverse the comparison operators in the while loop:
    len(names[j]) > key_length to len(names[j]) < key_length
"""


# -------------------
# Test Cases
# -------------------

print("Alphabetical Sort Test:")
test_names1 = ["John", "Travis", "Michael", "Mark", "Marcus"]
print("Input: ", test_names1)
print("Sorted:", alphabetical_sort(test_names1[:]))  # [:] to pass a copy so original isn't modified

print("\nSort by Length Test:")
test_names2 = ["John", "Travis", "Michael", "Mark", "Marcus"]
print("Input: ", test_names2)
print("Sorted by length:", sort_names_by_length(test_names2[:]))
