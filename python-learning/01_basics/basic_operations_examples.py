"""
Python Basics Starter Guide

This script covers:
- Variable declaration and types
- Basic operations and functions
- Conditionals and Boolean logic
- Loops
- Logical operators and comparisons
- Functions: declaration, parameters, return values
"""

print("hello")

# -----------------------------------
# Variables and Data Types
# -----------------------------------

a = 3
print(a)

str1 = "Hello World"
print(str1)

b, c, d = 5, 6.4, "Major"
print(b)
print(d)

print("{} {}".format("Value is", b))

print(type(a))   # <class 'int'>
print(type(b))   # <class 'int'>
print(type(c))   # <class 'float'>
print(type(d))   # <class 'str'>

print("{} {}".format("value is:", b))
print(f"value is: {b}")

# -----------------------------------
# Functions Demo
# -----------------------------------

# A function is a group of related statements that performs a specific task.

# Example 1: Function with parameter and printing output
def GreetUser(username):
    # Prints a greeting message using the provided username
    print("Hello, " + username + "! Welcome to the Python course.")

GreetUser("John")

# Example 2: Function that adds two integers and prints the result
# Note: This function does NOT return a value, so result cannot be stored/reused
def addIntegers(a, b):
    print(a + b)

addIntegers(2, 3)

# Example 3: Function that multiplies two integers and returns the result
# Using 'return' allows storing or reusing the output later
def multiplyIntegers(a, b):
    return a * b

print(multiplyIntegers(3, 4))

# -----------------------------------
# Example 1: Nested Function Calls
# -----------------------------------

def product(a, b):
    return a * b

print(product(product(2, 4), product(3, 5)))  # 120

# -----------------------------------
# Example 2: Functions with Arithmetic
# -----------------------------------

def difference(a, b):
    return a - b

def sum_new(a, b):
    return a + b

print(difference(sum_new(2, 2), sum_new(3, 3)))  # -2

# -----------------------------------
# Example 3: Boolean Comparison
# -----------------------------------

print((5 >= 2 * 4) and (5 <= 4 * 3))  # False

# -----------------------------------
# Example 4: Conditional Statement
# -----------------------------------

x = 3
if x + 5 > x ** 2 or x % 4 != 0:
    print("This comparison is True")

# -----------------------------------
# Example 5: if-elif-else Logic
# -----------------------------------

number = 6
if number * 2 < 14:
    print(number * 6 % 3)
elif number > 7:
    print(100 / number)
else:
    print(7 - number)

# -----------------------------------
# Function with remainder calculation
# -----------------------------------

def get_remainder(x, y):
    if x == 0 or y == 0 or x == y:
        remainder = 0
    else:
        remainder = (x % y) / y
    return remainder

print(get_remainder(10, 3))  # 0.3333...

# -----------------------------------
# While loop: Multiples of 5 up to 50
# -----------------------------------

multiplier = 1
result = multiplier * 5
while result <= 50:
    print(result)
    multiplier += 1
    result = multiplier * 5
print("Done")

# -----------------------------------
# Logical operators with strings and numbers
# -----------------------------------

print("yellow" > "cyan" and "brown" > "magneta")  # False
print(25 > 50 or 1 != 2)                          # True
print(not 42 == "answer")                          # True
