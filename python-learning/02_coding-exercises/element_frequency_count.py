# Question: Find frequency of each element in array
# Given an array, return a dictionary with elements as keys and their frequencies as values.
# Example: [2, 3, 2, 4, 3, 2] → {2: 3, 3: 2, 4: 1}

"""
Approach:
Create an empty dictionary to store frequencies.
Iterate through each element in the array.
For each element, increment its count in the dictionary.
If the element is not yet in the dictionary, initialize its count to 1.
Return the dictionary containing frequencies.
"""

def element_frequencies(arr):
    freq = {}
    for num in arr:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1
    return freq

# Time Complexity: O(n) where n is the length of the array
# Space Complexity: O(k) where k is the number of unique elements

# Test case
test_arr = [2, 3, 2, 4, 3, 2]
print("Output:", element_frequencies(test_arr))  # Output: {2: 3, 3: 2, 4: 1}

"""
Note:
This frequency counting logic works the same for arrays (lists) and strings, because both are iterable.
For numbers, simply convert the number to a string first (e.g., str(num)), then apply the same logic to count frequencies of each digit.
"""
