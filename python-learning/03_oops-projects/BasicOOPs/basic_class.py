# Basic Class Creation:
# Defines a blueprint for objects, grouping data (attributes) and behavior (methods) together.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

# Usage
p1 = Person("Alice", 30)
p1.greet()
