class Employee:
    def __init__(self, name):
        self.name = name

    def calculate_salary(self):
        return 50000

class Manager(Employee):
    def calculate_salary(self):
        return 80000

class Developer(Employee):
    def calculate_salary(self):
        return 70000


# Usage
e = Employee("John")
m = Manager("Sara")
d = Developer("Bob")

print(f"{e.name}'s salary: {e.calculate_salary()}")
print(f"{m.name}'s salary: {m.calculate_salary()}")
print(f"{d.name}'s salary: {d.calculate_salary()}")

"""
Method Overriding – "Customize inherited behavior"

Method overriding allows a child class to replace a method it inherited from a parent class. For example, a general Employee class has a calculate_salary() method, but a Manager or Developer may override it to provide specific salary logic.

This is essential when subclasses need to change or enhance the default behavior provided by a superclass.

It’s used when a shared interface is fine, but specific behavior must differ for different types of objects
"""
