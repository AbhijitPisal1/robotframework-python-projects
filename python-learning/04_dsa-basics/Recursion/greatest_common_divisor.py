# greatest common divisor of two numbers using recursion and Euclidean method
# What is Euclidean method: It is based on the principle that the GCD of two numbers also divides their difference.
# The method repeatedly replaces the larger number by the remainder of the division until the remainder is zero.
# At that point, the other number is the GCD.

def greatestCommonDivisor(a, b):
    assert int(a) == a and int(b) == b, 'The numbers must be integers only'
    if a < 0:
        a = -1 * a
    if b < 0:
        b = -1 * b
    if b == 0:
        return a
    else:
        return greatestCommonDivisor(b, a % b)

print(greatestCommonDivisor(44, 20))
"""
output explanation for greatestCommonDivisor(44, 20)
→ greatestCommonDivisor(20, 44 % 20) → greatestCommonDivisor(20, 4)
→ greatestCommonDivisor(4, 20 % 4) → greatestCommonDivisor(4, 0)
→ 4 (since b is 0, return a)
"""


"""
### Equivalent Iterative (Non-recursive) Version ###

def greatestCommonDivisor_iterative(a, b):
    assert int(a) == a and int(b) == b, 'The numbers must be integers only'
    a = abs(a)
    b = abs(b)
    while b != 0:
        a, b = b, a % b
    return a

print(greatestCommonDivisor_iterative(44, 20))  # Output: 4
"""