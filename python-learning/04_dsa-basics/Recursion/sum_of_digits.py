# sum of digits of positive integer numbers

def sumOfDigits(n):
    if n == 0:
        return 0
    else:
        return int(n%10)+sumOfDigits(int(n//10))

print(sumOfDigits(123))
"""
123 % 10  == 3      # remainder when 123 is divided by 10
123 // 10 == 12     # floor division: 123 divided by 10 is 12.3 → floor is 12
output explaination for sumOfDigits(123)
→ 3 + sumOfDigits(12)
→ 3 + 2 + sumOfDigits(1)
→ 3 + 2 + 1 + sumOfDigits(0)
→ 3 + 2 + 1 + 0 = 6

"""

"""
### Equivalent Iterative (Non-recursive) Version ###

def sumOfDigits_iterative(n):
    assert n >= 0 and int(n) == n, "Input must be a non-negative integer"
    total = 0
    while n > 0:
        total += n % 10
        n = n // 10
    return total

print(sumOfDigits_iterative(123))  # Output: 6
"""