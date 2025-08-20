# factorial of a positive integer using recursion

def factorial(n):
    assert 0 < n and int(n) == n, 'The number must be a positive integer'
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))

"""
output explanation for factorial(5)
→ 5 * factorial(4)
→ 5 * 4 * factorial(3)
→ 5 * 4 * 3 * factorial(2)
→ 5 * 4 * 3 * 2 * factorial(1)
→ 5 * 4 * 3 * 2 * 1 * factorial(0)
→ 5 * 4 * 3 * 2 * 1 * 1 = 120
"""

"""
### Equivalent Iterative (Non-recursive) Version ###

def factorial_iterative(n):
    assert 0 < n and int(n) == n, 'The number must be a positive integer'
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

print(factorial_iterative(5))  # Output: 120

"""