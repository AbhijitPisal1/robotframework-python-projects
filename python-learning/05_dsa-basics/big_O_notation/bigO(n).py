# O(n) - Linear time complexity
# number of operations increases as the input increases
# runs a loop n times, so it depends directly on the input size
# if input is 10, it runs 10 times; if input is 1000, it runs 1000 times
# not as fast as O(1), but still manageable for most cases

def print_items(n):
    for i in range(n):
        print(i)

print(print_items(10))
