def fibonacci(n):
    """Generate Fibonacci sequence up to n terms."""
    fib_sequence = []
    a, b = 0, 1
    for _ in range(n):
        fib_sequence.append(a)
        a, b = b, a + b  # Update values
    return fib_sequence

# Example usage:
num_terms = 10
result = fibonacci(num_terms)
print(f"Fibonacci sequence up to {num_terms} terms: {result}")  # Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]