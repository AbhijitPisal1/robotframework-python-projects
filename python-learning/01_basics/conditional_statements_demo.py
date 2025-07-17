"""
This code demonstrates conditional statements in Python using an integer variable:
1. Assigns a value to the variable "number".
2. Compares "number" against specific conditions using if-elif-else statements.
3. Prints appropriate messages based on the comparisons.
"""

# Assigns the value 25 to the variable "number"
number = 25

# Compares "number" to 5. If the condition is true, the block will execute.
if number <= 5:
    print("The number is 5 or smaller.")

# Compares "number" to 33. If true, this block executes.
elif number == 33:
    print("The number is 33.")

# Compares "number" to 32 and 6. If true, it prints the corresponding message.
elif number < 32 and number >= 6:
    print("The number is less than 32 and greater than 6.")

else:
    print("The number is " + str(number))

# Expected output:
# The number is less than 32 and greater than 6.