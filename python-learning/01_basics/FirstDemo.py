print("hello")

# Comments in Python start with #

# Declaring variables
a = 3            # No need to declare type explicitly; Python infers it
print(a)

str1 = "Hello World"
print(str1)

# Creating multiple variables in a single line
b, c, d = 5, 6.4, "Major"
print(b)
print(d)

# To concatenate variable values of different types in a print statement, use format()
print("{} {}".format("Value is", b))

# To know the type of variables
print(type(a))   # <class 'int'>
print(type(b))   # <class 'int'>
print(type(c))   # <class 'float'>
print(type(d))   # <class 'str'>

# Note:
# The following will cause an error because you can't concatenate str and int directly
# print("value of b is " + b)  # TypeError

# Instead, use format() or f-strings (Python 3.6+)
print("{} {}".format("value is:", b))
# or
print(f"value is: {b}")
