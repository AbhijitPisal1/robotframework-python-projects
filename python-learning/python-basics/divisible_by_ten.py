# Generates a list of integers from 1 to 100 that are divisible by 10.
# List Comprehension with Conditional Statement
print("List comprehension result:")

# This single line of list comprehension replaces multiple lines:
print([ x for x in range(1,101) if x % 10 == 0 ])

# Long form for loop with nested if-statement
print("Long form code result:")

# The list comprehension achieves the same result as this longer version:
my_list = []
for x in range(1,101):
    if x % 10 == 0:
        my_list.append(x)
print(my_list)

'''
Created on Jul 18, 2023

@author: APisal
'''