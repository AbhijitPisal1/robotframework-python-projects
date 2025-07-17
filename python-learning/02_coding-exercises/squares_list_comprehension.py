# This list comprehension generates a list of squared numbers (n*n)
# and takes two integer parameters.

def squares(start, end):
    # The list comprehension computes the square of an integer "n,"
    # which ranges from "start" to "end" inclusively.
    # To include the endpoint in range(), add +1 to the end value.
    return [n * n for n in range(start, end + 1)]


print(squares(2, 3))  # Should output [4, 9]
print(squares(1, 5))  # Should output [1, 4, 9, 16, 25]
print(squares(0, 10))  # Should output [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

'''
Created on Jul 18, 2023

@author: APisal
'''