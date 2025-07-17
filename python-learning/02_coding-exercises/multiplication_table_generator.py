"""
This function prints a multiplication table for numbers ranging from 'start' to 'stop'.
It uses nested loops to calculate and display the products, arranged in a tabular format.
Each row corresponds to a number in the range, and each column shows the product of that number with the other numbers from the range.
"""

def multiplication_table(start, stop):
    # Iterate through each number from start to stop (inclusive) for the outer loop
    for x in range(start, stop + 1):  
        # Iterate through each number from start to stop (inclusive) for the inner loop
        for y in range(start, stop + 1):
            # Print the product of x and y, followed by a space (no new line)
            print(str(x * y), end=" ")
        # Print an empty line after each row to separate the rows
        print()

# Call the function to print the multiplication table from 1 to 3
multiplication_table(1, 3)
# Should print:
# 1 2 3 
# 2 4 6 
# 3 6 9 

'''
Created on Jul 18, 2023

@author: APisal
'''