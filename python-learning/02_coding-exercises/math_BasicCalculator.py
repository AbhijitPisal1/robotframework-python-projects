"""
Understanding class creation in Python
Create a basic calculator class to perform addition, subtraction, multiplication, and division.
Each method should return the result of the operation.
Each method should return the result of the operation.
Create an instance of the BasicCalculator class and demonstrate the functionality of each method.

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
