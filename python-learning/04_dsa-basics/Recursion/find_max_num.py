# find the maximum number in an array using recursion

import array

def findMaxNum(arr, n):
    if n == 1:
        return arr[0]
    else:
        return max(arr[n-1], findMaxNum(arr, n-1))

array1 = array.array('i', [21, 11, 23, 10, 7])
print(findMaxNum(array1, 5))

"""
output explanation for findMaxNum([21, 11, 23, 10, 7], 5)
→ max(7, findMaxNum([21, 11, 23, 10], 4))
→ max(10, findMaxNum([21, 11, 23], 3))
→ max(23, findMaxNum([21, 11], 2))
→ max(11, findMaxNum([21], 1)) → returns 21
→ max(11, 21) = 21
→ max(23, 21) = 23
→ max(10, 23) = 23
→ max(7, 23) = 23
→ final result = 23
"""


"""
### Equivalent Iterative (Non-recursive) Version ###

import array

def findMaxNum_iterative(arr):
    assert len(arr) > 0, "Array must not be empty"
    max_num = arr[0]
    for num in arr[1:]:
        if num > max_num:
            max_num = num
    return max_num

array1 = array.array('i', [21, 11, 23, 10, 7])
print(findMaxNum_iterative(array1))  # Output: 23
"""