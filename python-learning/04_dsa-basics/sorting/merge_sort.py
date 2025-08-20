def merge_sort(arr):
    """
    Perform a merge sort on the input list.
    Merge sort is a divide-and-conquer algorithm that divides the list into halves,
    recursively sorts each half, and then merges the sorted halves back together.

    Time Complexity:
        - Worst, Average, and Best Case: O(n log n), where n is the number of elements.
          This is because the list is repeatedly split in half (log n splits)
          and merging takes O(n) at each level.

    Space Complexity:
        - O(n) additional space for the temporary arrays used during merging.

    When to Use:
        - Large datasets where stable and predictable O(n log n) performance is needed.
        - When stable sorting is required (equal elements keep their original order).
        - Suitable for linked lists as it does not require random access.

    When Not to Use:
        - Small datasets where simpler algorithms like insertion or bubble sort can be faster due to lower overhead.
        - Memory-constrained environments since it requires extra space.

    Example:
        Input: [2, 1, 7, 6, 4, 5, 3, 4]

        Stepwise:
        Split into [2,1,7,6] and [4,5,3,4]
        Recursively sort each half and merge:
        [2,1,7,6] → [1,2,6,7]
        [4,5,3,4] → [3,4,4,5]
        Merge [1,2,6,7] and [3,4,4,5] → [1,2,3,4,4,5,6,7]
    """
    if len(arr) > 1:
        mid = len(arr) // 2  # Find midpoint

        # Split array into left and right halves
        left_half = arr[:mid]
        right_half = arr[mid:]

        # Recursive call on left half
        merge_sort(left_half)
        # Recursive call on right half
        merge_sort(right_half)

        i = j = k = 0  # i for left_half, j for right_half, k for arr

        # Merge the two sorted halves into original array
        while i < len(left_half) and j < len(right_half):
            if left_half[i] <= right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # Copy any remaining elements from left_half
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        # Copy any remaining elements from right_half
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

        # Print current merged state of array after each merge step
        print(f"Merged: {arr}")


# Sample input list to demonstrate the algorithm
sample_list = [2, 1, 7, 6, 4, 5, 3, 4]

# Call the merge sort function on sample input
merge_sort(sample_list)

# Expected output (prints after each merge step):
# Merged: [2, 1]
# Merged: [1, 2]
# Merged: [6, 7]
# Merged: [1, 2, 6, 7]
# Merged: [4, 5]
# Merged: [3, 4]
# Merged: [3, 4, 4, 5]
# Merged: [1, 2, 3, 4, 4, 5, 6, 7]

"""
Note if question asked in different manners:
To sort in ascending order, keep comparison as <= when merging.
To sort in descending order, reverse comparison in merging step: use >= instead of <=.
"""
