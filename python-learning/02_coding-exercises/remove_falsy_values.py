# Problem: Remove all falsy values from a list
# Input: [0, 1, False, 2, '', 3, None, 4]
# Output: [1, 2, 3, 4]

"""
Approach:
Falsy values in Python include 0, False, '', None, empty containers, etc.
To remove falsy values from the list, we iterate through each element and
keep only those that evaluate to True in a boolean context.
We create a new list by checking each element's truthiness using a simple if condition.
This approach ensures the original list is not modified in place.
"""

def remove_falsy_values(lst):
    result = []
    for item in lst:
        if item:  # only append truthy values
            result.append(item)
    return result

# Time Complexity: O(n), where n is the length of the list
# Space Complexity: O(n), for storing the filtered list

# Test case
test_input = [0, 1, False, 2, '', 3, None, 4]
print(remove_falsy_values(test_input))  # Expected output: [1, 2, 3, 4]


"""
Note:
If the input is a number, convert it to string or list of digits first,
then apply the same logic to remove falsy (zero) digits.
For example:
    num = 1761809445678028873
    digits = list(str(num))
    filtered_digits = [d for d in digits if d != '0']  # remove zero digits
"""