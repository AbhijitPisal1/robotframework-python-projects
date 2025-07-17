# This function generates a matrix of numbers using nested for loops and the range() function.
# The upper limit in range() is inclusive, filling both rows and columns.
def matrix(initial_number, end_of_first_row):

    # Assigns longer parameter names to shorter variables for convenience.
    n1 = initial_number 
    n2 = end_of_first_row + 1  # Includes the upper limit by adding 1

    # The outer loop creates the columns.
    for column in range(n1, n2):

        # The inner loop generates the rows.
        for row in range(n1, n2):

            # Adds a space between numbers for readability, overriding the default newline behavior.
            print(column * row, end=" ")

        # Ends the row upon reaching the upper limit; a print() function triggers a new line.
        print()


# Calls the function with two integers.
matrix(1, 4)
# Expected output:
# 1 2 3 4 
# 2 4 6 8 
# 3 6 9 12 
# 4 8 12 16

'''
Created on Jul 18, 2023

@author: APisal
'''