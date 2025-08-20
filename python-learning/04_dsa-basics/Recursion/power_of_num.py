# calculate the power of a given number using recursion
def powerOfNum(base, exp):
    assert int(exp) == exp, 'The exponent should be integer number only'
    if exp == 0:
        return 1
    elif exp < 0:
        return 1/base * powerOfNum(base, exp+1)
    return base * powerOfNum(base, exp-1)

print(powerOfNum(4, 4))
print(powerOfNum(4, -3))

"""
output explanation for powerOfNum(4, 4)
→ 4 * powerOfNum(4, 3)
→ 4 * 4 * powerOfNum(4, 2)
→ 4 * 4 * 4 * powerOfNum(4, 1)
→ 4 * 4 * 4 * 4 * powerOfNum(4, 0)
→ 4 * 4 * 4 * 4 * 1 = 256

output explanation for powerOfNum(4, -3)
→ (1/4) * powerOfNum(4, -2)
→ (1/4) * (1/4) * powerOfNum(4, -1)
→ (1/4) * (1/4) * (1/4) * powerOfNum(4, 0)
→ (1/4) * (1/4) * (1/4) * 1 = 0.015625
"""



"""
### Equivalent Iterative (Non-recursive) Version ###

def powerOfNum_iterative(base, exp):
    assert int(exp) == exp, 'The exponent should be an integer only'
    result = 1
    is_negative = exp < 0
    exp = abs(exp)

    for _ in range(exp):
        result *= base

    if is_negative:
        return 1 / result
    return result

print(powerOfNum_iterative(4, 4))    # Output: 256
print(powerOfNum_iterative(4, -3))   # Output: 0.015625
"""