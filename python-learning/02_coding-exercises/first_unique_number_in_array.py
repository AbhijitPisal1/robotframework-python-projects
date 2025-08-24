# Question: First unique number in a given array
# Given an array, find the first number that appears only once.
# Example: [2, 5, 1, 2, 3, 5] → 1

"""
Approach:
First, count the occurrences of each number by iterating through the array once using a dictionary.
Then iterate through the array a second time, checking the count of each element.
The first element with a count of 1 is the first unique number.
If no unique number is found, return None.
This approach requires two passes over the array but ensures the correct order is preserved.
"""

def first_unique_number(arr):
    count_dict = {}
    for num in arr:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1

    for num in arr:
        if count_dict[num] == 1:
            return num
    return None

# Time Complexity: O(n) where n is the length of the array
# Space Complexity: O(n) for the dictionary storing counts

# Test case
test_arr = [2, 5, 1, 2, 3, 5]
print("Output:", first_unique_number(test_arr))  # Output: 1

"""
Note:
To apply this logic for a number (e.g. 234567987654234567), convert the number to a string:
    for digit in str(number): ...
Then use the same logic to find the first unique digit.
"""
