"""
Average Calculator
Objective: Calculate the average of three numbers.

Instructions:
Create a function called CalculateAverage that takes three parameters: num1, num2, and num3.
Use the numbers 10,20,30 as input to functions
The function should return the average of these three numbers.

Expected Output:
The average of 10, 20, and 30 is 20.0
"""
def CalculateAverage(num1, num2, num3):
    return (num1 + num2 + num3) / 3

# Using the numbers 10, 20, 30
average = CalculateAverage(10, 20, 30)

print(f"The average of 10, 20, and 30 is {average}")
