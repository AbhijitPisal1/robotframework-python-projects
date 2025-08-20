def print_items(a, b):
    for i in range(a):
        print(i)

    for j in range(b):
        print(j)

print(print_items(3, 4))

# O(a + b) - linear time complexity with two different inputs
# two separate loops → not nested → so we add their runtimes
# time depends on both a and b individually
# if a = 3 and b = 4, total operations = 3 + 4 = 7

# if loops were nested instead:
"""
def print_items(a, b):
    for i in range(a):
        for j in range(b):
            print(i, j)

print(print_items(4, 5))
"""

# O(a * b) - nested loop → multiply runtimes
# If Algorithm says "do this, then do that" → add → O(a + b)
# If Algorithm says "do this for each time you do that" → multiply → O(a * b)
