def selection_sort(arr):
    """
    Perform an in-place selection sort on the input list.

    Selection Sort works by repeatedly finding the minimum element from the unsorted portion
    of the list and swapping it with the first unsorted element, thus growing the sorted portion
    from the front of the list.

    Time Complexity:
        - Worst, Average, Best Case: O(n^2), where n is the number of elements.
          Because it always scans the unsorted portion to find the minimum.
    Space Complexity:
        - O(1) since sorting is done in place without extra storage.

    When to Use:
        - Small datasets where simplicity is more important than efficiency.
        - Situations where memory write operations are costly, since selection sort
          does at most n swaps.

    When Not to Use:
        - Large datasets, as the algorithm is inefficient compared to O(n log n) sorts.

    Example:
        Input: [2, 1, 7, 6, 4, 5, 3, 4]

        Pass 1: Minimum element 1 found at index 1, swap with element at index 0:
            [1, 2, 7, 6, 4, 5, 3, 4]

        Pass 2: Minimum element 2 found at index 1 (already in place, swap with itself)
            [1, 2, 7, 6, 4, 5, 3, 4]

        Pass 3: Minimum element 3 found at index 6, swap with element at index 2:
            [1, 2, 3, 6, 4, 5, 7, 4]

        Pass 4: Minimum element 4 found at index 4, swap with element at index 3:
            [1, 2, 3, 4, 6, 5, 7, 4]

        Pass 5: Minimum element 4 found at index 7, swap with element at index 4:
            [1, 2, 3, 4, 4, 5, 7, 6]

        Pass 6: Minimum element 5 found at index 5 (already in place)
            [1, 2, 3, 4, 4, 5, 7, 6]

        Pass 7: Minimum element 6 found at index 7, swap with element at index 6:
            [1, 2, 3, 4, 4, 5, 6, 7]
    """
    n = len(arr)
    for i in range(n):
        # Assume the min element is at the start of unsorted portion
        min_index = i

        # Find the index of the minimum element in the unsorted portion
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        # Swap the found minimum element with the first element of unsorted portion
        arr[i], arr[min_index] = arr[min_index], arr[i]

        # Print the list after each pass to demonstrate the progress
        print(f"After pass {i + 1}: {arr}")


# Sample input list to demonstrate the algorithm
sample_list = [2, 1, 7, 6, 4, 5, 3, 4]

# Call the selection sort function on sample input
selection_sort(sample_list)

# Expected output stepwise (print after each pass):
# After pass 1: [1, 2, 7, 6, 4, 5, 3, 4]
# After pass 2: [1, 2, 7, 6, 4, 5, 3, 4]
# After pass 3: [1, 2, 3, 6, 4, 5, 7, 4]
# After pass 4: [1, 2, 3, 4, 6, 5, 7, 4]
# After pass 5: [1, 2, 3, 4, 4, 5, 7, 6]
# After pass 6: [1, 2, 3, 4, 4, 5, 7, 6]
# After pass 7: [1, 2, 3, 4, 4, 5, 6, 7]

"""
Note:
Selection sort always selects the minimum element from the unsorted portion to place at the
beginning of the unsorted portion.

If you want to sort in descending order, just change the comparison to:
    if arr[j] > arr[min_index]:
        min_index = j
"""
