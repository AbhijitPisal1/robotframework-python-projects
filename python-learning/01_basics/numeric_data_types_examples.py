# EXAMPLES OF NUMERIC DATA TYPES
print("EXAMPLES OF NUMERIC DATA TYPES")

""" Python numeric data types are used to hold numeric values like:
    int - holds signed integers of non-limited length.
    float - holds floating point numbers and they are accurate up to 15 decimal places.
    complex - holds complex numbers.
"""
# Creating a variable with an integer value.
a = 100
print("The type of variable having value", a, "is", type(a))  # Output: <class 'int'>

# Creating a variable with a float value.
b = 10.2345
print("The type of variable having value", b, "is", type(b))  # Output: <class 'float'>

# Creating a variable with a complex value.
c = 100 + 3j
print("The type of variable having value", c, "is", type(c))  # Output: <class 'complex'>

# Arithmetic operations with integers and floats
addition_result = a + b
print("Addition of", a, "and", b, "is:", addition_result)  # Output: 110.2345

# Complex number operations
complex_result = c * 2
print("Multiplying complex number", c, "by 2 gives:", complex_result)  # Output: (200+6j)

# Converting different numeric types
int_to_float = float(a)  # Converting integer to float
print("Integer converted to float:", int_to_float)  # Output: 100.0

float_to_int = int(b)  # Converting float to integer (truncating)
print("Float converted to integer:", float_to_int)  # Output: 10
