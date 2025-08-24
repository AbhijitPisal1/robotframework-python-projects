######################## CLASS DEMO: CALCULATOR ##############################
# Classes in Python are user-defined blueprints or prototypes.
# They encapsulate data and behavior (via methods) into a single structure.
# This demo class 'Calculator' performs operations like summation, and uses:
# - Constructor (__init__)
# - Instance variables (specific to each object)
# - Class variables (shared across all objects)
# - Methods (functions defined inside a class)
class Calculator:
    num1 = 100  # Class variable (shared by all instances of the class)

    # Default constructor (__init__):
    # Automatically called when an object is created.
    # 'self' refers to the current object instance.
    def __init__(self, a, b):
        self.firstNumber = a       # Instance variable (unique to each object)
        self.secondNumber = b
        print("This is default constructor")

    # Instance method: general method inside the class
    def getData(self):
        print("now executing a method in class")

    # Method to compute the summation
    def Summation(self):
        # Access instance variables with 'self'
        # Access class variable via 'self' or class name
        return self.firstNumber + self.secondNumber + self.num1
        #return self.firstNumber + self.secondNumber + Calculator.num1      # class variable can be called from class name instead of self


######################## OBJECT CREATION AND METHOD CALLS ##############################

# Creating the first object of the Calculator class
obj = Calculator(2, 3)
obj.getData()                          # Calls a method
print(obj.Summation())                 # Calls a method and prints result: 2 + 3 + 100 = 105

# Creating a second object with different values
obj = Calculator(4, 5)
obj.getData()
print(obj.Summation())                 # Output: 4 + 5 + 100 = 109

