# linear search - sequential
# items searched one by one - works on sorted and unsorted arrays

def linearSearch(array, value):
    """
    Performs linear search on a list to find the index of the given value.
    Returns the index if found, otherwise -1.
    """
    for i in range(len(array)):
        if array[i] == value:
            return i
    return -1

print(linearSearch([20, 30, 40, 25, 10, 15], 10))

"""
output explanation for linearSearch([20, 30, 40, 25, 10, 15], 10)
→ checks array[0] = 20 (not 10)
→ checks array[1] = 30 (not 10)
→ checks array[2] = 40 (not 10)
→ checks array[3] = 25 (not 10)
→ checks array[4] = 10 (found)
→ returns index 4
"""

"""
Notes:
1. Lists, strings, and tuples are ordered and indexed, so linear search returns the element’s index.
2. Sets and dictionaries are unordered and don’t support indexing, so linear search can only check if a value or key is present.
3. For sets and dicts, membership testing (using 'in') is faster and preferred over searching by iteration.

Bonus Tips :
1. For strings, str.find() does similar work but only for characters or substrings.
2. For large unsorted datasets, linear search is inefficient (O(n)). If the list is sorted, binary search is a better choice (O(log n)).
3. Python’s native in keyword uses optimized implementations (like C loops under the hood) — so in practice, you’d often just do:
    if value in array:
        # do something
"""