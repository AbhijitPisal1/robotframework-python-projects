# This function rounds a number up to the nearest multiple of 10.
def round_up(number):
    x = 10
    # Floor division gives the integer part of "number" divided by x; for example, 35 // 10 equals 3.
    whole_number = number // x
    # The modulo operator finds the remainder of "number" divided by x; for instance, 35 % 10 equals 5.
    remainder = number % x
    # If the remainder is 5 or more:
    if remainder >= 5:
        # Round up by returning x times (whole_number + 1)
        return x * (whole_number + 1)
    # Otherwise, return x times whole_number to round down.
    return x * whole_number


# Calls the function with 35, expecting an output of 40.
print(round_up(35))  # Should print 40

'''
Created on Jul 17, 2023

@author: APisal
'''