# O(n^2) - Quadratic time complexity
# nested loops → n * n = n^2 operations performed
# if input is 5, inner loop runs 5 times for each of 5 outer loops → 25 times total
# if we add one more loop → becomes n^3 (cubic), and so on
# still written as O(n^2) even if more layers exist, because we focus on the highest growth factor
# as input grows, operations grow much faster (quadratically)

def print_items(n):
    for i in range(n):
        for j in range(n):
            print(i, j)

print(print_items(5))
