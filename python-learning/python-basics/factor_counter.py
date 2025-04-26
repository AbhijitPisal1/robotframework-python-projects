"""This function counts the integer factors of a variable
"given_number" passed as a parameter. The return value "count" 
includes "given_number" itself as a factor (n*1)."""


def count_factors(given_number):
    """Initialize "factor" to 1 to include "given_number" as a
    factor (starting at 2 would exclude it)."""
    factor = 1
    count = 1

    """Returns 0 factors if "given_number" is 0."""
    if given_number == 0:
        return 0

    """While "factor" is less than "given_number", check for 
    factors using the modulo operator %."""
    while factor < given_number:
        """If "given_number" is divisible by "factor", increment 
        the factor count."""
        if given_number % factor == 0:
            count += 1
        """Increment "factor" to check the next possible factor."""
        factor += 1

    """Return the final count of factors."""
    return count


print(count_factors(0))  # Count value will be 0
print(count_factors(3))  # Should count 2 factors (1x3)
print(count_factors(10))  # Should count 4 factors (1x10, 2x5)
print(count_factors(24))  # Should count 8 factors (1x24, 2x12, 3x8,
# and 4x6). 

'''
Created on Jul 17, 2023

@author: APisal
'''