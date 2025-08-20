# Method Overriding:
# A child class provides a specific implementation of a method
# already defined in its parent class to alter or extend behavior.

class Parent:
    def greet(self):
        print("Hello from Parent")

class Child(Parent):
    def greet(self):
        print("Hello from Child")

p = Parent()
c = Child()

p.greet()  # Hello from Parent
c.greet()  # Hello from Child (overridden)
