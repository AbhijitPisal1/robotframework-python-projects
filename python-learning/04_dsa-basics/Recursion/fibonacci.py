# fibonacci number using recursion for non-negative integers

def fibonacci(n):
    assert 0 <= n and int(n) == n, 'Fibonacci number cannot be negative or non-integer'
    if n in [0, 1]:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(5))

"""
output explanation for fibonacci(5)
→ fibonacci(5) = fibonacci(4) + fibonacci(3)
→ fibonacci(4) = fibonacci(3) + fibonacci(2)
→ fibonacci(3) = fibonacci(2) + fibonacci(1)
→ fibonacci(2) = fibonacci(1) + fibonacci(0)
→ fibonacci(1) = 1, fibonacci(0) = 0
→ fibonacci(2) = 1 + 0 = 1
→ fibonacci(3) = 1 + 1 = 2
→ fibonacci(4) = 2 + 1 = 3
→ fibonacci(5) = 3 + 2 = 5
→ final result = 5
"""

"""
### Equivalent Iterative (Non-recursive) Version ###

def fibonacci_iterative(n):
    assert 0 <= n and int(n) == n, 'Fibonacci number cannot be negative or non-integer'
    if n == 0:
        return 0
    elif n == 1:
        return 1
    prev, curr = 0, 1
    for _ in range(2, n + 1):
        prev, curr = curr, prev + curr
    return curr

print(fibonacci_iterative(5))  # Output: 5
"""