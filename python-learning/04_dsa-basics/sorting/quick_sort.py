def quick_sort(arr):
    """
    Perform an in-place quick sort on the input list.
    Quick sort works by selecting a pivot element and partitioning the list so that
    elements less than or equal to the pivot come before it, and elements greater come after.
    It then recursively sorts the sublists on either side of the pivot.

    Time Complexity:
        - Average and Best Case: O(n log n), where n is the number of elements.
        - Worst Case: O(n^2), when the pivot selections are poor (e.g., already sorted list).

    Space Complexity:
        - O(log n) due to recursion stack space.

    When to Use:
        - Large datasets where average performance matters.
        - When in-place sorting is desired without extra memory.

    When Not to Use:
        - Very small datasets where simpler sorts like insertion sort may be faster.
        - When guaranteed worst-case performance is needed (use merge sort or heap sort).

    Note if question asked in different manners:
        To sort in ascending order, use the condition `arr[j] <= pivot` in the partition function.
        To sort in descending order, use the condition `arr[j] >= pivot` in the partition function.
    """

    def partition(array, low, high):
        pivot = array[high]  # pivot element
        i = low - 1          # index of smaller element
        # Loop to compare each element with pivot
        for j in range(low, high):
            # Change the comparison operator to > for descending order
            if array[j] <= pivot:
                i += 1
                array[i], array[j] = array[j], array[i]
        # Place pivot after the last smaller element
        array[i + 1], array[high] = array[high], array[i + 1]
        return i + 1

    def quick_sort_recursive(array, low, high):
        if low < high:
            pi = partition(array, low, high)
            print(f"Pivot {array[pi]} placed at index {pi}: {array}")
            quick_sort_recursive(array, low, pi - 1)
            quick_sort_recursive(array, pi + 1, high)

    quick_sort_recursive(arr, 0, len(arr) - 1)


# Sample input list to demonstrate the algorithm
sample_list = [5, 3, 8, 4, 2, 7, 1, 10]

# Call quick_sort function on sample input
quick_sort(sample_list)

# Expected output after each pivot placement:
# Pivot 4 placed at index 3: [3, 2, 1, 4, 5, 7, 8, 10]
# Pivot 1 placed at index 0: [1, 2, 3, 4, 5, 7, 8, 10]
# Pivot 3 placed at index 2: [1, 2, 3, 4, 5, 7, 8, 10]
# Pivot 10 placed at index 7: [1, 2, 3, 4, 5, 7, 8, 10]
# Pivot 7 placed at index 5: [1, 2, 3, 4, 5, 7, 8, 10]
# Pivot 5 placed at index 4: [1, 2, 3, 4, 5, 7, 8, 10]
# Pivot 8 placed at index 6: [1, 2, 3, 4, 5, 7, 8, 10]

print("Sorted array:", sample_list)
