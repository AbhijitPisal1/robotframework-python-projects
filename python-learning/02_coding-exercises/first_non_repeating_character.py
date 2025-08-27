# Question: Find the first non-repeating character in a string.

def first_non_repeating_character(s):
    """Find the first non-repeating character in a string using a frequency map."""
    frequency = {}

    # Count the frequency of each character in the string
    for char in s:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1

    # Find the first character with a frequency of 1
    for char in s:
        if frequency[char] == 1:
            return char
    return None  # Return None if there are no non-repeating characters


# Example usage:
input_string = "swiss"
result = first_non_repeating_character(input_string)
print(
    f"The first non-repeating character in '{input_string}' is: '{result}'")  # Output: The first non-repeating character in 'swiss' is: 'w'.