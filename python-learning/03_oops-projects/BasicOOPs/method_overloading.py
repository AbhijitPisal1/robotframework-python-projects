class Calculator:
    def add(self, a, b=0, c=0):
        return a + b + c

# Usage
calc = Calculator()

print(calc.add(5, 10))         # 15
print(calc.add(1, 2, 3))       # 6
print(calc.add(100))           # 100

"""
Method Overloading (Simulated in Python) – "One method, different arguments"

Python doesn’t support traditional method overloading (same method name with different signatures), but it can be simulated using default parameters or *args.

For example, a Calculator class might define a single add() method that can handle two or three numbers, depending on what's passed in. It’s convenient for providing flexible APIs without writing multiple versions of the same method.

Use this when you want a method to behave differently based on the number or type of arguments passed.
"""