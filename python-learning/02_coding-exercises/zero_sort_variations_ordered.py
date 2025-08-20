"""
This module provides functions to reorder lists of integers or digits within a number,
moving zeroes either to the front or back while sorting the non-zero elements.

Core approach used in all functions:
- Separate zero elements/digits from non-zero ones.
- Sort the non-zero elements using insertion sort (demonstrated explicitly).
- Concatenate zero elements either before or after the sorted non-zero elements.

Time Complexity: O(n^2) due to insertion sort.
Space Complexity: O(n) for auxiliary lists to hold separated elements.
"""
# --------------------------
# VARIATION 1: List of Integers
# Move zeroes to back, rest sorted ascending (core implementation)
# --------------------------

def move_zeros_back_sort_asc_list(arr):
    non_zero = []
    zero_count = 0

    # Separate zeros and non-zeros
    for num in arr:
        if num == 0:
            zero_count += 1
        else:
            non_zero.append(num)

    # Sort non-zero elements using insertion sort (ascending)
    for i in range(1, len(non_zero)):
        key = non_zero[i]
        j = i - 1
        while j >= 0 and non_zero[j] > key:
            non_zero[j + 1] = non_zero[j]
            j -= 1
        non_zero[j + 1] = key

    return non_zero + [0] * zero_count

# Test
print(move_zeros_back_sort_asc_list([1, 0, 2, 0, 3, 5, 0, 4, 0]))
# Expected: [1, 2, 3, 4, 5, 0, 0, 0, 0]

"""
NOTES for VARIATION 1:
- To move zeros to the front instead of back:
    Change final return to:
        return [0] * zero_count + non_zero

- To sort in descending order instead of ascending:
    Change comparison in insertion sort from:
        while j >= 0 and non_zero[j] > key:
    to:
        while j >= 0 and non_zero[j] < key:
"""

# --------------------------
# VARIATION 2: Number Input (digits)
# Move zero digits to back, rest sorted ascending (core implementation)
# --------------------------

def move_zero_digits_back_sort_asc(num):
    num_str = str(num)
    zero_count = 0
    non_zeros = []

    # Separate zeros and non-zero digits
    for ch in num_str:
        if ch == '0':
            zero_count += 1
        else:
            non_zeros.append(ch)

    # Insertion sort non-zero digits ascending
    for i in range(1, len(non_zeros)):
        key = non_zeros[i]
        j = i - 1
        while j >= 0 and non_zeros[j] > key:
            non_zeros[j + 1] = non_zeros[j]
            j -= 1
        non_zeros[j + 1] = key

    return ''.join(non_zeros + ['0'] * zero_count)

# Test
print(move_zero_digits_back_sort_asc(10230405))  # Expected: '12345000'

"""
NOTES for VARIATION 2:
- To move zeros to the front instead of back:
    Change final return to:
        return ''.join(['0'] * zero_count + non_zeros)

- To sort digits in descending order:
    Change comparison in insertion sort from:
        while j >= 0 and non_zeros[j] > key:
    to:
        while j >= 0 and non_zeros[j] < key:
"""

