# This function generates a string of all numbers from "minimum" to "maximum", inclusive.

def all_numbers(minimum, maximum):
    return_string = ""  # Initializes an empty string.

    # Loop through the range including "maximum".
    for num in range(minimum, maximum + 1):
        return_string += str(num) + " "  # Append each number followed by a space to return_string.

    # Removes the trailing space at the end of return_string.
    return return_string.strip()


print(all_numbers(2, 6))  # Should be 2 3 4 5 6
print(all_numbers(3, 10))  # Should be 3 4 5 6 7 8 9 10
print(all_numbers(-1, 1))  # Should be -1 0 1
print(all_numbers(0, 5))  # Should be 0 1 2 3 4 5
print(all_numbers(0, 0))  # Should be 0

'''
Created on Jul 18, 2023

@author: APisal
'''