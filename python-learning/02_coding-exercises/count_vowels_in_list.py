# Question: Count vowels in each string in a list
# Given a list of strings, count the number of vowels (a, e, i, o, u) in each string.
# Return a list of counts corresponding to each string.
# Example: ["apple", "banana", "grape"] → [2, 3, 2]

"""
Approach:
Define a set of vowels for quick membership checking.
Iterate through each string in the list.
For each string, iterate through its characters and count how many are vowels.
Store the vowel count for each string in a result list.
Return the list of vowel counts.
"""

def count_vowels_in_list(strings):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    counts = []
    for s in strings:
        count = 0

        for char in s.lower():  #iterating over each character in the string s one by one
            if char in vowels:
                count += 1
        counts.append(count)
    return counts

# Time Complexity: O(n * m) where n is number of strings and m is average length of each string
# Space Complexity: O(n) for the output list of counts

# Test case
test_strings = ["apple", "banana", "grape"]
print("Output:", count_vowels_in_list(test_strings))  # Output: [2, 3, 2]