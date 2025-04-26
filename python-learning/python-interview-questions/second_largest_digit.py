# Question: Find the Second Largest Digit in a String
# For example, if the input is "str1025rts", the output should be 2.

def second_largest_digit(s):
    # Step 1: Initialize a set to store unique digits found in the string.
    digits = set()

    # Step 2: Iterate through each character in the string.
    for char in s:
        # Step 3: Check if the character is a digit.
        if char.isdigit():
            # Step 4: Add the digit to the set of digits.
            digits.add(int(char))

    # Step 5: Convert the set back to a sorted list.
    sorted_digits = sorted(digits)

    # Step 6: Check if there are at least two unique digits.
    if len(sorted_digits) < 2:
        return None  # Not enough digits to find a second largest.

    # Step 7: Return the second largest digit.
    return sorted_digits[-2]


# Example usage
input_string = "hi279364s9"
result = second_largest_digit(input_string)
print(result)  # This should output 2




"""Alterntively
def second_largest_digit(s):
    # Step 1: Initialize variables to track the largest and second largest digits.
    largest = second_largest = -1

    # Step 2: Iterate through each character in the string.
    for char in s:
        # Step 3: Check if the character is a digit.
        if char.isdigit():
            digit = int(char)
            # Step 4: Update largest and second largest accordingly.
            if digit > largest:
                second_largest = largest
                largest = digit
            elif largest > digit > second_largest:
                second_largest = digit

    # Step 5: Check if a second largest digit was found.
    return second_largest if second_largest != -1 else None

# Example usage
input_string = "hi279364s9"
result = second_largest_digit(input_string)
print(result)  # This should output 7
"""