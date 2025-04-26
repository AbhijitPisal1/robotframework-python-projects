# Example 1
# Calculate the output of this print statement

def product(a, b):
    return (a * b)


print(product(product(2, 4), product(3, 5)))


#################################

# Example 2 
# Determine the output of this print statement

def difference(a, b):
    return (a - b)


def sum_new(a, b):
    return (a + b)


print(difference(sum_new(2, 2), sum_new(3, 3)))

#################################

# Example 3
# Check the Boolean result of this comparison

print((5 >= 2 * 4) and (5 <= 4 * 3))

#################################

# Example 4 
# Assess the value of the comparison in the if statement 

x = 3
if x + 5 > x ** 2 or x % 4 != 0:
    print("This comparison is True")

#################################

# Example 5 
# Evaluate the output from this if-elif-else statement

number = 6
if number * 2 < 14:
    print(number * 6 % 3)
elif number > 7:
    print(100 / number)
else:
    print(7 - number)


# Click Run to verify your answers. If you encounter issues
# calculating manually, please review the Practice Quiz 
# Study Guides, videos, and readings in this Module.

def get_remainder(x, y):
    if x == 0 or y == 0 or x == y:
        remainder = 0
    else:
        remainder = (x % y) / y
    return remainder


print(get_remainder(10, 3))

multiplier = 1
result = multiplier * 5
while result <= 50:
    print(result)
    multiplier += 1
    result = multiplier * 5
print("Done")

# This while loop displays multiples of 5 up to 50. The
# "multiplier" starts at 1, and "result" is initialized 
# as the product of "multiplier" and 5. The loop continues 
# while "result" is less than or equal to 50. Inside the loop, 
# it prints "result," increments "multiplier" by 1, and updates 
# "result" to the new "multiplier" multiplied by 5. When 
# the condition is no longer met, the loop ends, and "Done" 
# is printed.