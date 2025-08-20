# convert a number from decimal to binary using recursion

def convertDecimalToBinary(n):
    assert int(n) == n, 'The parameter must be an integer only'
    if n == 0:
        return 0
    else:
        return n % 2 + 10 * convertDecimalToBinary(int(n / 2))

print(convertDecimalToBinary(10))
"""
output explanation for convertDecimalToBinary(10)
→ 10 % 2 = 0, so 0 + 10 * convertDecimalToBinary(5)
→ 5 % 2 = 1, so 0 + 10 * (1 + 10 * convertDecimalToBinary(2))
→ 2 % 2 = 0, so 0 + 10 * (1 + 10 * (0 + 10 * convertDecimalToBinary(1)))
→ 1 % 2 = 1, so 0 + 10 * (1 + 10 * (0 + 10 * (1 + 10 * convertDecimalToBinary(0))))
→ convertDecimalToBinary(0) = 0
→ So, last part is 1 + 10 * 0 = 1
→ Next, 0 + 10 * 1 = 10
→ Then, 1 + 10 * 10 = 101
→ Finally, 0 + 10 * 101 = 1010
"""

"""
### Equivalent Iterative (Non-recursive) Version ###

def convertDecimalToBinaryIterative(n):
    assert int(n) == n, 'The parameter must be an integer only'
    binary = 0
    place = 1
    while n > 0:
        remainder = n % 2
        binary += remainder * place
        n //= 2
        place *= 10
    return binary

print(convertDecimalToBinaryIterative(10))  # Output: 1010

"""
