# Question: Handle different scenarios where zeroes must be moved while preserving the order of non-zero elements.
#
# Variants:
# 1. Move all zero digits to the front in a number → e.g., 10230405 → "00012345"
# 2. Move all zero digits to the back in a number → e.g., 10230405 → "12345000"
# 3. Move all zero elements to the front in a list → e.g., [1, 0, 2] → [0, 1, 2]
# 4. Move all zero elements to the back in a list → e.g., [1, 0, 2] → [1, 2, 0]

# -----------------------------------------------------
# Explanation of the Logic (Applies to all variations):
# 1. Convert the input (number or list) into a form that allows iteration.
# 2. Traverse through each digit or element:
#    - Count the number of zeroes.
#    - Store all non-zero items in order.
# 3. Construct the final output:
#    - For moving zeroes to the **front**: prepend zeroes before non-zero items.
#    - For moving zeroes to the **back**: append zeroes after non-zero items.
#
# Note:
# - For numbers, results are returned as strings to preserve leading zeros.
# - For lists, results are returned as new or modified lists (in-place when possible).
#
# Time Complexity: O(n)
# Space Complexity: O(n) for digit manipulation; O(1) for in-place list operations
# -----------------------------------------------------

# 1. Move zero digits to the front in a number
def move_zeros_to_front_in_number(number):
    num_str = str(number)
    zero_count = 0
    non_zero_digits = []

    for digit in num_str:
        if digit == '0':
            zero_count += 1
        else:
            non_zero_digits.append(digit)

    result_digits = ['0'] * zero_count + non_zero_digits
    return ''.join(result_digits)

"""
NOTES for VARIATION 2 Move zero digits to the back in a number:
- To move zeros to the back instead of front:
    Change final return to:
        return ''.join(non_zeros+ ['0'] * zero_count)
"""

# 3. Move zero elements to the front in a list
def move_zeros_to_front_in_list(arr):
    count_zero = 0
    non_zero_elements = []

    for num in arr:
        if num == 0:
            count_zero += 1
        else:
            non_zero_elements.append(num)

    return [0] * count_zero + non_zero_elements
"""
NOTES for VARIATION 4 Move zero elements to the back in a list:
- To move zeros to the back instead of front:
    Change final return to:
        return non_zero_elements + [0] * count_zero
    However this creates new lists and Uses O(n) extra space.
"""
# 4. Move zero elements to the back in a list
def move_zeros_to_back_in_list(arr):
    write_index = 0  # Where to write next non-zero

    for read_index in range(len(arr)):
        if arr[read_index] != 0:
            arr[write_index] = arr[read_index]
            write_index += 1

    while write_index < len(arr):
        arr[write_index] = 0
        write_index += 1

    return arr

# -----------------------------------------------------
# Test Section

print("----- Number: Move Zeros to Front -----")
print(move_zeros_to_front_in_number(10230405))  # Expected: "00012345"

print("----- List: Move Zeros to Front -----")
print(move_zeros_to_front_in_list([1, 0, 2, 0, 3, 5, 0, 4, 0]))  # Expected: [0, 0, 0, 0, 1, 2, 3, 5, 4]

print("----- List: Move Zeros to Back -----")
print(move_zeros_to_back_in_list([1, 0, 2, 0, 3, 5, 0, 4, 0]))   # Expected: [1, 2, 3, 5, 4, 0, 0, 0, 0]
