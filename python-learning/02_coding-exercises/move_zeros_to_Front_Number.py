# Question: Given a number, move all zero digits to the front,
# while maintaining the relative order of the non-zero digits.
#
# Input: A number (e.g., 10230405)
# Output: A number with all zeros at the front, rest digits in order
# Example: Input: 10230405 → Output: 00012345

# -----------------------------------------------------
# Explanation of the Logic:
# 1. Convert the number to a string to iterate through each digit.
# 2. Traverse the digits one by one:
#    - Count how many zeroes there are.
#    - Store all non-zero digits in a list to maintain their order.
# 3. After traversal, prepend the counted number of zeroes to the non-zero digits.
# 4. Join everything to form the final string, and convert it back to an integer if needed.
#
# Note: Leading zeroes in a number will be lost if we keep it as an integer.
#       So, we return the result as a string to preserve leading zeroes.
# -----------------------------------------------------

def move_zeros_to_front(number):
    # Convert number to string to process digits
    num_str = str(number)
    print(num_str)

    zero_count = 0
    non_zero_digits = []

    # Traverse each digit
    for digit in num_str:
        if digit == '0':
            zero_count += 1
        else:
            non_zero_digits.append(digit)
            print(non_zero_digits)

    # Construct result with zeroes at front
    result_digits = ['0'] * zero_count + non_zero_digits
    result_str = ''.join(result_digits)

    return result_str  # Return as string to preserve leading zeros

# -----------------------------------------------------
# Time Complexity: O(n), where n is the number of digits in the number
# Space Complexity: O(n), to store non-zero digits and construct result
# -----------------------------------------------------

# Test Case
test_input = 10230405
expected_output = "00012345"

output = move_zeros_to_front(test_input)
print("Input:        ", test_input)
print("Expected Out: ", expected_output)
print("Actual Out:   ", output)
