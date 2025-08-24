# Question: Sort strings in descending lexicographical order
# Input: ["0000", "2919", "53", "4341", "786"]
# Output: ["786", "53", "4341", "2919", "0000"]

"""
Approach:
We are required to sort a list of strings in descending lexicographical order without using Python shortcuts like sorted() or reversed().
Lexicographical order means dictionary-like order, where comparison is made character by character based on ASCII values.
To solve this, we implement insertion sort:
- We start from the second element and move leftward comparing strings using standard string comparison (s1 > s2).
- For descending order, we place a string before others only if it is greater in lexicographical comparison.
- Strings like "786" > "53" because '7' > '5' in ASCII, and so on.

This approach demonstrates an understanding of string comparison and sorting mechanics.

Time Complexity: O(n^2) – Insertion sort on n strings
Space Complexity: O(1) – In-place sorting with constant space
"""

def sort_strings_desc_lex(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] < key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# Test Case
test_input = ["0000", "2919", "53", "4341", "786"]
result = sort_strings_desc_lex(test_input)
print("Output:", result)  # Expected: ["786", "53", "4341", "2919", "0000"]


"""
NOTE:
If you want to sort the strings based on their numeric value (e.g., "53" < "786" because 53 < 786),
then in the comparison condition you should convert the strings to integers:

Change:
    while j >= 0 and arr[j] < key:
To:
    while j >= 0 and int(arr[j]) < int(key):

This will sort the list descending by numeric value instead of lexicographical order.
"""
