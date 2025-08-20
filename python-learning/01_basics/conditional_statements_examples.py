"""
This file demonstrates various conditional statements in Python using:
1. Integer comparisons with if-elif-else.
2. String comparison in an if-else.
3. Grading system using chained conditions.
"""

######################## DEMO 1: Integer Comparison ##############################
# Assigns the value 25 to the variable "number"
number = 25

# Compares "number" using if-elif-else
if number <= 5:
    print("The number is 5 or smaller.")
elif number == 33:
    print("The number is 33.")
elif number < 32 and number >= 6:
    print("The number is less than 32 and greater than 6.")
else:
    print("The number is " + str(number))

# Expected output:
# The number is less than 32 and greater than 6.


######################## DEMO 2: String Comparison ##############################
# Simple if-else check for string equality
greeting = "Good Morning"

if greeting == "Morning":
    print("Condition matches")
else:
    print("Condition does not match")
print("If-else condition code is completed")


######################## DEMO 3: Grade Evaluation ##############################
# Chained conditions to assign grades based on marks
marks = 75

if marks <= 100 and marks > 90:
    print("A Grade")
elif marks <= 90 and marks > 75:
    print("B Grade")
elif marks <= 75 and marks > 60:
    print("C Grade")
elif 60 >= marks > 45:
    print("D Grade")
elif marks <= 45:
    print("E Grade")

print("Evaluation done")
