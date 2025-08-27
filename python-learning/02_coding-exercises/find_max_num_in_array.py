# Question: Find the biggest number in a given array without using max(arr)
# Given an array of integers, return the largest number without using the built-in max() function.
# Input example: [3, 10, 6, 2, 8]
# Output: 10

"""
Approach:
To find the biggest number manually, initialize a variable to the first element of the array.
Then iterate through each element in the array, and if an element is greater than the current biggest number,
update the biggest number.
After checking all elements, the variable holds the maximum value.
This approach ensures a single pass through the array.

Time Complexity: O(n) where n is the length of the array
Space Complexity: O(1) since only a single variable is used for tracking
"""

def find_biggest_number(arr):
    if len(arr) == 0:
        raise ValueError("Array cannot be empty")

    biggest = arr[0]
    for num in arr:
        if num > biggest:
            biggest = num
    return biggest

"""
Note: 
To find the smallest number instead, simply change the comparison operator in the if condition:
     if num < smallest:
         smallest = num
and initialize a variable named 'smallest' instead of 'biggest'.
 See the next function for a full example.

"""
# Test case
test_arr = [3, 10, 6, 2, 8]
print("Output:", find_biggest_number(test_arr))  # Output: 10


###########     Variation: Find the maximum digit in a single number    ###########
def find_max_digit(num):
    num_str = str(num)
    max_digit = int(num_str[0])
    for digit_char in num_str:
        digit = int(digit_char)
        if digit > max_digit:
            max_digit = digit
    return max_digit

test_num = 826052479263
print("Max digit in number:", find_max_digit(test_num))      # Output: 9
