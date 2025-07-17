# Question: Write a program to find the factorial of a number.

def factorial(n):
    """Calculate the factorial of a non-negative integer n."""
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    elif n == 0 or n == 1:
        return 1  # Base case: 0! = 1 and 1! = 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i  # Multiply result by each integer up to n
        return result

# Example usage:
number = 5
fact = factorial(number)
print(f"The factorial of {number} is {fact}.")  # Output: The factorial of 5 is 120.



"""" recursion code snippet would be 
def factorial(n) :
    if n < 0:
        return None  # Factorial is not defined for negative numbers
    if n == 0 or n == 1:
        return 1  # Base case
    return n * factorial(n - 1)  # Recursive case

# Example usage:
number = 5
result = factorial(number)
print(f"Factorial of {number} is {result}")  # Output: 120
"""