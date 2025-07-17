# This recursive function calculates the sum of all positive integers up to a given number n.
# It returns the sum of numbers from 1 to n, where n is greater than or equal to 1.
def sum_positive_numbers(n):
    if n <= 1:
        return n 
    else:
        return n + sum_positive_numbers(n-1)

print(sum_positive_numbers(3)) # Should be 6
print(sum_positive_numbers(5)) # Should be 15

'''
Created on Jul 18, 2023

@author: APisal
'''