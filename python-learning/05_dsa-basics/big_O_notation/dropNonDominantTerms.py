# O(n^2 + n) - combined time complexity
# first part (nested loop): O(n^2) → runs n * n times
# second part (single loop): O(n) → runs n times
# total time = O(n^2 + n)
# we drop the non-dominant part → O(n) is much smaller than O(n^2) as n grows
# final Big O = O(n^2) → dominant term only
# helps simplify and focus on what affects performance the most

def print_items(n):
    for i in range(n):
        for j in range(n):
            print(i, j)
    for k in range(n):
        print(k)

print(print_items(5))


