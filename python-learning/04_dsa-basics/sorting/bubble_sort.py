def bubble_sort(arr):
    """
    Perform an in-place bubble sort on the input list.
    Bubble sort works by repeatedly swapping adjacent elements if they are in the wrong order.
    Each pass through the list moves the largest unsorted element to its correct position at the end.
    Time Complexity:
        - Worst and Average Case: O(n^2), where n is the number of elements.
          This occurs when the list is in reverse order.
        - Best Case: O(n) if the list is already sorted (with an optimized version).
    Space Complexity:
        - O(1) as sorting is done in place without extra storage.
    When to Use:
        - Small or nearly sorted datasets
        - When simplicity is more important than efficiency
    When Not to Use:
        - Large datasets where more efficient algorithms like quicksort are preferred
    Example:
        Input: [4, 3, 2, 1]
        After first pass: [3, 2, 1, 4]  # Largest element 4 bubbled to the end
        After second pass: [2, 1, 3, 4]
        After third pass: [1, 2, 3, 4]
    """
    n = len(arr)
    # Outer loop for each pass through the list
    for i in range(n):
        # Initialize swapped flag to False before this pass
        # This flag tracks whether any swaps happen during the current pass
        swapped = False

        # Inner loop to compare adjacent elements up to the unsorted portion
        for j in range(0, n - i - 1):
            # If current element is greater than next, swap them
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True  # Mark that a swap happened this pass

        # Print the state of the list after each full outer loop pass
        print(f"After pass {i + 1}: {arr}")

        # If no swaps occurred, it means the list is already sorted
        # So we can stop the algorithm early to save unnecessary passes
        if not swapped:
            break


# Sample input list to demonstrate the algorithm
sample_list = [2, 1, 7, 6, 4, 5, 3, 4]

# Call the bubble sort function on sample input
bubble_sort(sample_list)

# Expected output stepwise (print after each pass):
# After pass 1: [1, 2, 6, 4, 5, 3, 4, 7]
# After pass 2: [1, 2, 4, 5, 3, 4, 6, 7]
# After pass 3: [1, 2, 4, 3, 4, 5, 6, 7]
# After pass 4: [1, 2, 3, 4, 4, 5, 6, 7]
# After pass 5: [1, 2, 3, 4, 4, 5, 6, 7]
# (Stops early because no swaps happened on pass 5)


"""
Note if question asked in different manners:
To sort in ascending order, use the condition arr[j] > arr[j + 1] 
To sort in descending order, use the condition to arr[j] < arr[j + 1]
"""