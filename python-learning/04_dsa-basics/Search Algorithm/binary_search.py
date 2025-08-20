# binary search
# - faster useful for sorted arrays
# - finds the index of value in a sorted array by repeatedly dividing the search interval in half until the value is found or the interval is empty.

# binary search on a sorted list

def binarySearch(array, value):
    """
    Performs binary search on a sorted array to find the index of the given value.
    Returns the index if found, otherwise -1.
    """
    assert array == sorted(array), "Binary search requires a sorted array"
    start = 0
    end = len(array) - 1
    while start <= end:
        middle = (start + end) // 2
        if array[middle] == value:
            return middle
        elif value < array[middle]:
            end = middle - 1
        else:
            start = middle + 1
    return -1

custArray = [2, 5, 8, 12, 16, 23, 38]
print(binarySearch(custArray, 16))

"""
output explanation for binarySearch(custArray, 16)
→ start=0, end=6, middle=3 → array[middle]=12 (16 > 12)
→ start=4, end=6, middle=5 → array[middle]=23 (16 < 23)
→ start=4, end=4, middle=4 → array[middle]=16 (found)
→ returns index 4
"""

"""
Notes:
1. Binary search works only on sorted arrays or lists. If the input is unsorted, results are incorrect.
2. It has a time complexity of O(log n), which is much faster than linear search (O(n)) for large datasets.
3. Binary search returns the index of one occurrence of the value. If duplicates exist, it may not find all of them.
4. For small or unsorted datasets, linear search may be simpler and sometimes more efficient.
5. Binary search can be implemented iteratively or recursively.
6. Always ensure the input is sorted before applying binary search.
"""
