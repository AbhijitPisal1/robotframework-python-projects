"""
Working with Lists
Create a list named fruits that contains five different fruit names (strings):
    "apple", "banana", "cherry", "date", "elderberry"
Print the first and last elements of the list.
Use slicing to print the second and third fruits from the list.

Expected Result:
First fruit: apple
Last fruit: elderberry
Fruits from index 1 to 2: ['banana', 'cherry']
"""

fruits = ["apple", "banana", "cherry", "date", "elderberry"]

# Print the first and last elements
print(f"First fruit: {fruits[0]}")
print(f"Last fruit: {fruits[-1]}")

# Use slicing to print the second and third fruits
print(f"Fruits from index 1 to 2: {fruits[1:3]}")
