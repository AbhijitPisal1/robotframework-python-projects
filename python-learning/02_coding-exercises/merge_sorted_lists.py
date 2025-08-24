# Question: Merge two sorted lists into one sorted list
# Without using sorted() on final result
# list1 = [1, 4, 2]
# list2 = [6, 3, 5]

"""
Explanation:
First, the input lists may not be sorted, so we need to sort each list individually without using sorted() on the final combined list.
We will implement a simple sorting function (like insertion sort) for each list to ensure they are sorted.
After sorting both lists, we merge them in a classic two-pointer approach, comparing elements one by one to produce a final sorted merged list.
This approach ensures we don't use Python's built-in sorted() on the combined list but rely on sorting individual lists first, then merging.

Time Complexity: O(n^2) due to insertion sort on each list + O(n) merge
Space Complexity: O(n) for the merged output list
"""

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def merge_sorted_lists(list1, list2):
    # Sort both lists individually using insertion sort
    insertion_sort(list1)
    insertion_sort(list2)

    merged = []
    i, j = 0, 0
    # Merge the two sorted lists
    while i < len(list1) and j < len(list2):
        if list1[i] <= list2[j]:
            merged.append(list1[i])
            i += 1
        else:
            merged.append(list2[j])
            j += 1
    # Append remaining elements
    while i < len(list1):
        merged.append(list1[i])
        i += 1
    while j < len(list2):
        merged.append(list2[j])
        j += 1
    return merged

# Test case
list1 = [1, 4, 2]
list2 = [6, 3, 5]
result = merge_sorted_lists(list1, list2)
print(result)  # Expected output: [1, 2, 3, 4, 5, 6]


"""
Note on handling numbers and strings:

- For numbers:
  Convert each number to a list of digits using:
      digits = [int(d) for d in str(number)]
  Then apply the sorting and merging functions on these digit lists.
  Finally, join the merged list back to form a number if needed.

- For strings:
  Each string can be treated as a list of characters directly.
  Apply sorting and merging functions as is.
  Join the merged list back into a string if needed.

The core sorting and merging logic remains unchanged.
Only input preparation (number → digit list) and final conversion differ.
"""
