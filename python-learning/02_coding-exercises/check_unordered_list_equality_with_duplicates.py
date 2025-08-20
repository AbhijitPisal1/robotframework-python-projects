# Problem:
# 25. Check if two lists are equal (unordered, duplicates allowed)
# Given two lists, determine if they contain the same elements with the same frequencies,
# regardless of order.
# Example: [1, 2, 2, 3] and [3, 2, 1, 2] → True
#          [1, 2, 2, 3] and [3, 2, 1, 1] → False

"""
Approach:
Count the frequency of each element in both lists using dictionaries.
Compare the two frequency dictionaries.
If they are identical, the lists are equal (unordered, with duplicates allowed).
Otherwise, they are not equal.
"""

def are_lists_equal_unordered(list1, list2):
    def frequency_dict(lst):
        freq = {}
        for item in lst:
            if item in freq:
                freq[item] += 1
            else:
                freq[item] = 1
        return freq

    freq1 = frequency_dict(list1)
    print(freq1)
    freq2 = frequency_dict(list2)
    print(freq2)
    return freq1 == freq2

# Time Complexity: O(n + m) where n and m are lengths of the two lists
# Space Complexity: O(k) where k is the number of unique elements in the lists

# Test case
list_a = [1, 2, 2, 3]
list_b = [3, 2, 1, 2]
print("Output:", are_lists_equal_unordered(list_a, list_b))  # Output: True