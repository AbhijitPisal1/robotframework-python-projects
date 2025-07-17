# O(log n) - logarithmic time complexity
# uses divide and conquer technique
# list is divided into half each time → search space gets smaller quickly
# as number of elements increases, operations increase slowly (much slower than linear)
# for example: for 8 elements → takes max 3 steps; for 16 → max 4 steps
# very efficient for large data sets

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1  # target not found

# example call
print(binary_search([1, 3, 5, 7, 9, 11], 7))


