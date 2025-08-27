# Question: Generate a list of prime numbers up to a given limit (without using shortcuts)
# Given a number `limit`, generate all prime numbers from 2 up to that number.
# Avoid using any shortcuts like the Sieve of Eratosthenes, square root optimization, or built-in helpers.
# Example: limit = 10 → [2, 3, 5, 7]

"""
Approach:
Define a function `is_prime(n)` that checks if a number is prime by testing divisibility
from 2 to n-1. If the number is divisible by any of these, it is not prime.

Define another function `get_primes_up_to(limit)` that:
- Iterates from 2 to the given limit.
- For each number, uses `is_prime()` to check if it's a prime.
- If it is, append it to the list of primes.
- Finally, return the list of primes.

This approach demonstrates the fundamental logic for finding prime numbers
without relying on optimizations or advanced techniques. It is ideal for learning and clarity.
"""

def is_prime(n):
    if n <= 1:
        return False  # 0 and 1 are not prime numbers
    for i in range(2, n):
        if n % i == 0:
            return False  # n is divisible by some number other than 1 and itself
    return True  # n is prime

def get_primes_up_to(limit):
    primes = []
    number = 2
    while number <= limit:
        if is_prime(number):
            primes.append(number)
        number += 1
    return primes

# Example usage:
limit = 50
prime_numbers = get_primes_up_to(limit)
print("Prime numbers up to", limit, ":", prime_numbers)
