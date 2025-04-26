# Question: Merge Two Arrays
# For instance, if you have arr1 = [5, 3, 2] and arr2 = [9, 0, 1],
# the task is to merge them into one array, resulting in [5, 3, 2, 9, 0, 1].

def merge_arrays(arr1, arr2):
    # Step 1: Use the '+' operator to concatenate the two arrays.
    merged_array = arr1 + arr2

    # Step 2: Return the merged array.
    return merged_array


# Example usage
arr1 = [5, 4, 2, 3]
arr2 = [9, 0, 1]
result = merge_arrays(arr1, arr2)
print(result)  # This should output [5, 3, 2, 9, 0, 1]