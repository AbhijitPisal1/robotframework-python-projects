# space complexity is measure of amount of working storage that an algorithm needs

# Example 1: Recursive function (uses O(n) space)
def sum1(n):
    if n <= 0:
        return 0
    return n + sum1(n - 1)

sum1(3)

# O(n) space complexity
# every recursive call waits for the next call, so calls stack up in memory
# n calls means n stack frames are stored at once

# Example 2: Iterative function calling another function in a loop (O(1) space)
def pair_sum_sequence(n):
    total = 0
    for i in range(n):
        # each call to pair_sum exists one at a time, finishes, and is removed from memory
        total = total + pair_sum(i, i + 1)
    return total

def pair_sum(a, b):
    return a + b

print(pair_sum_sequence(4))

# O(1) space complexity
# even though pair_sum is called n times, only one call is in memory at any moment
# calls do not exist simultaneously on the call stack
# because loop calls run one after another, not waiting on each other
# so memory does not grow with input size


# Optimized recursive sum using tail recursion concept
def sum_tail(n, accumulator=0):
    if n <= 0:
        return accumulator
    return sum_tail(n - 1, accumulator + n)

print(sum_tail(3))

# Still O(n) space in Python due to no tail call optimization
# but this version is easier to optimize in some languages or with manual stack handling

# Summary:
# - Recursive calls add up in memory → O(n) space
# - Loop calls run one after another → O(1) space
