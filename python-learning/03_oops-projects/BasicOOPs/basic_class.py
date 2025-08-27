# Basic Class Creation:
# Defines a blueprint for objects, grouping data (attributes) and behavior (methods) together.

class Person:
    
    """
    Default Constructor: The default constructor is a special method __init__ that is automatically called when an instance of a class is created. It initializes the instance variables of the class. In this case, it takes two parameters, a and b, which are used to set the values of firstNumber and secondNumber.
    """
    def __init__(self, name, age):
        """ Self: The self keyword refers to the current instance of the class. It is used to access instance variables and methods from within the class. For example, self.firstNumber refers to the firstNumber attribute of the specific instance, allowing methods to access that instance's data."""
        
        
        self.name = name
        self.age = age
        """
        Instances: Instances are the specific objects created from a class. Each instance maintains its own state (values for instance variables)
        """

    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

# Usage
p1 = Person("Alice", 30)
p1.greet()
