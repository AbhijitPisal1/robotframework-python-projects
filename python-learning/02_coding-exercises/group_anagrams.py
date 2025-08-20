# Problem:
# 27. Group words that are anagrams
# Given a list of words, group them so that each group contains words that are anagrams of each other.
# Example: ["eat", "tea", "tan", "ate", "nat", "bat"]
# Output: [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]

"""
Approach:
Anagrams have the same characters in the same frequency.
For each word, create a key by sorting its characters (this will be the same for all anagrams).
Use a dictionary to map each sorted key to a list of words (anagrams).
Iterate through the words, add them to the appropriate group.
Return the list of grouped anagrams.

"""

def group_anagrams(words):
    anagram_map = {}
    for word in words:
        # Create a sorted tuple of characters as the key
        key_chars = list(word)
        # Sort characters manually using simple sorting algorithm (e.g., insertion sort) to avoid shortcuts
        for i in range(1, len(key_chars)):
            current = key_chars[i]
            j = i - 1
            while j >= 0 and key_chars[j] > current:
                key_chars[j + 1] = key_chars[j]
                j -= 1
            key_chars[j + 1] = current
        key = tuple(key_chars)

        if key in anagram_map:
            anagram_map[key].append(word)
        else:
            anagram_map[key] = [word]

    return list(anagram_map.values())

# Time Complexity: O(n * m^2) where n is number of words and m is max length of a word (due to insertion sort)
# Space Complexity: O(n * m) for storing groups and keys

# Test case
test_words = ["eat", "tea", "tan", "ate", "nat", "bat"]
print("Output:", group_anagrams(test_words))
# Output: [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]


"""
Note on handling numbers:
If the input list contains numbers instead of strings, convert each number to string before passing
to this function, e.g.:

# Input list of numbers
input_numbers = [123, 321, 213, 456, 654, 789]

# Convert numbers to strings without shortcuts
words_as_strings = []
for num in input_numbers:
    words_as_strings.append(str(num))
    
group_anagrams(words_as_strings)

This way, the existing code works without any modification.
"""