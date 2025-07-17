# O(n) - Linear time complexity (after dropping constants)
# drop constant - also called removing constants in Big O
# time taken is n + n = 2n → written as O(2n)
# but we remove constant factors → becomes O(n)
# even if there are two separate loops, they are not nested → still linear
# dropping constants helps focus on growth rate, not exact counts
# O(n) can sometimes be faster than O(1) depending on input, but O(1) is still best in theory

def print_items(n):
    for i in range(n):
        print(i)

    for j in range(n):
        print(j)

print(print_items(5))
