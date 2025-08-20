def insertion_sort(arr):
    """
    Perform an in-place insertion sort on the input list.

    Insertion Sort works by building a sorted portion at the front of the list.
    It takes one element from the unsorted portion at a time and inserts it
    into the correct position within the sorted portion by shifting larger elements.

    Time Complexity:
        - Worst and Average Case: O(n^2), where n is the number of elements.
          This happens when the list is sorted in reverse order.
        - Best Case: O(n) if the list is already sorted (only one comparison per element).
    Space Complexity:
        - O(1) since sorting is done in place without extra storage.

    When to Use:
        - Small or nearly sorted datasets (efficient in such cases).
        - When simplicity and ease of implementation are more important than speed.

    When Not to Use:
        - Large datasets where more efficient algorithms like mergesort or quicksort are preferred.

    Example:
        Input: [2, 3, 5, 8, 4, 1, 6, 9, 7]

        Pass 1: Insert 3 into sorted [2] → [2, 3, 5, 8, 4, 1, 6, 9, 7]
        Pass 2: Insert 5 into sorted [2, 3] → no change
        Pass 3: Insert 8 into sorted [2, 3, 5] → no change
        Pass 4: Insert 4 into sorted [2, 3, 5, 8]
                Shift 8, 5 to right, insert 4 → [2, 3, 4, 5, 8, 1, 6, 9, 7]
        Pass 5: Insert 1 into sorted [2, 3, 4, 5, 8]
                Shift all right, insert 1 → [1, 2, 3, 4, 5, 8, 6, 9, 7]
        Pass 6: Insert 6 into sorted [1, 2, 3, 4, 5, 8]
                Shift 8 right, insert 6 → [1, 2, 3, 4, 5, 6, 8, 9, 7]
        Pass 7: Insert 9 into sorted [1, 2, 3, 4, 5, 6, 8]
                No change
        Pass 8: Insert 7 into sorted [1, 2, 3, 4, 5, 6, 8, 9]
                Shift 9, 8 right, insert 7 → [1, 2, 3, 4, 5, 6, 7, 8, 9]
    """
    n = len(arr)
    # Traverse from second element to end (since first element is trivially sorted)
    for i in range(1, n):
        key = arr[i]  # Current element to insert
        j = i - 1

        # Shift elements of the sorted portion that are greater than key to the right
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        # Insert key into its correct position
        arr[j + 1] = key

        # Print the state of the list after inserting the current element
        print(f"After pass {i}: {arr}")


# Sample input list to demonstrate the algorithm
sample_list = [2, 3, 5, 8, 4, 1, 6, 9, 7]

# Call the insertion sort function on sample input
insertion_sort(sample_list)

# Expected output stepwise (print after each pass):
# After pass 1: [2, 3, 5, 8, 4, 1, 6, 9, 7]
# After pass 2: [2, 3, 5, 8, 4, 1, 6, 9, 7]
# After pass 3: [2, 3, 5, 8, 4, 1, 6, 9, 7]
# After pass 4: [2, 3, 4, 5, 8, 1, 6, 9, 7]
# After pass 5: [1, 2, 3, 4, 5, 8, 6, 9, 7]
# After pass 6: [1, 2, 3, 4, 5, 6, 8, 9, 7]
# After pass 7: [1, 2, 3, 4, 5, 6, 8, 9, 7]
# After pass 8: [1, 2, 3, 4, 5, 6, 7, 8, 9]


"""
Note:
To sort in descending order, change the comparison in the while loop to:
    while j >= 0 and arr[j] < key:
        arr[j + 1] = arr[j]
        j -= 1
"""
