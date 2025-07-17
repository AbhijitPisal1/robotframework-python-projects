"""
Understanding class creation in Python
Objective: Create a basic calculator class to perform addition, subtraction, multiplication, and division.

Instructions:
Create a class named BasicCalculator.
Define a constructor that initializes two numbers. Use numbers 10 & 5
Implement methods for:
Addition
Subtraction
Multiplication
Division

Each method should return the result of the operation.
Create an instance of the BasicCalculator class and demonstrate the functionality of each method.

Example Output:

Addition: 10 + 5 = 15
Subtraction: 10 - 5 = 5
Multiplication: 10 * 5 = 50
Division: 10 / 5 = 2.0
"""

class BasicCalculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def addition(self):
        return self.num1 + self.num2

    def subtraction(self):
        return self.num1 - self.num2

    def multiplication(self):
        return self.num1 * self.num2

    def division(self):
        # Handle division by zero just in case
        if self.num2 == 0:
            return "Error: Division by zero"
        return self.num1 / self.num2

# Create an instance with 10 and 5
calc = BasicCalculator(10, 5)

# Demonstrate functionality
print(f"Addition: {calc.num1} + {calc.num2} = {calc.addition()}")
print(f"Subtraction: {calc.num1} - {calc.num2} = {calc.subtraction()}")
print(f"Multiplication: {calc.num1} * {calc.num2} = {calc.multiplication()}")
print(f"Division: {calc.num1} / {calc.num2} = {calc.division()}")
