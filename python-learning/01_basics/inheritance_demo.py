# Importing the Calculator class
from Python_Tutorials.calculator_class_demo import Calculator

# ChildImpl class inherits from Calculator, meaning it gains access to Calculator's methods and variables
class ChildImpl(Calculator):
    num2 = 200  # Additional class variable unique to ChildImpl

    # Constructor for ChildImpl
    def __init__(self):
        # Explicitly call the parent class constructor with specific values for firstNumber and secondNumber
        Calculator.__init__(self, 2, 10)

    # New method in ChildImpl to calculate a combined sum
    def getCompleteData(self):
        # Uses:
        # - num2 (ChildImpl's class variable)
        # - num1 (Calculator's class variable)
        # - Summation() method from Calculator (returns firstNumber + secondNumber + num1)
        return self.num2 + self.num1 + self.Summation()


# Create an instance of ChildImpl
obj = ChildImpl()

# Print the result of getCompleteData
print(obj.getCompleteData())  # Expected output: 200 + 100 + (2 + 10 + 100) = 412



# Inheritance in Python allows a class (called the child or subclass) to inherit attributes and methods
# from another class (called the parent or superclass). This promotes code reuse and logical hierarchy.

# Benefits of inheritance include:
# - Reusability: avoid duplicating code by extending existing classes.
# - Extensibility: add or customize behavior in child classes.
# - Maintainability: logically group related classes in a hierarchy.