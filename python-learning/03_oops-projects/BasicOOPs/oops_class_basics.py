# Problem:
# 37. Write a basic class with __init__, and add a method - to test Python OOP — e.g., class Employee
"""
Explanation:
We will create a class Employee with an __init__ method to initialize employee attributes like name and salary.
We will also add a method called display_info to return a formatted string showing employee details.
This demonstrates basic object-oriented programming concepts: class definition, instance variables, and instance methods.

Time Complexity: O(1) for initialization and method calls
Space Complexity: O(1) for each instance's attributes
"""

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def display_info(self):
        return f"Employee Name: {self.name}, Salary: {self.salary}"

# Test case
emp = Employee("Alice", 70000)
print(emp.display_info())  # Expected output: Employee Name: Alice, Salary: 70000