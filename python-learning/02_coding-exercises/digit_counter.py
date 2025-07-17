# Counts the number of digits in a positive integer, including zero.
def digits(n):
    count = 0
    if n == 0:
        count += 1  # Special case for zero, which has 1 digit
    while n != 0:
        n = n // 10  # Remove the last digit from the number
        count += 1  # Increment the digit count for each removed digit
    return count  # Return the total count of digits

print(digits(25))   # Should print 2
print(digits(144))  # Should print 3
print(digits(1000)) # Should print 4
print(digits(0))    # Should print 1

'''
Created on Jul 18, 2023

@author: APisal
'''