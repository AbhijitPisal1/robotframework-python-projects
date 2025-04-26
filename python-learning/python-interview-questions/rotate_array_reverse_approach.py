# Question: Rotate an array given an integer k using the reverse approach.

def rotate_array(nums, k):
    """Rotate the array to the right by k steps using the reverse approach."""
    n = len(nums)
    k = k % n  # Normalize k to handle cases where k is greater than the array length

    # Reverse the entire array
    reverse(nums, 0, n - 1)
    # Reverse the first k elements
    reverse(nums, 0, k - 1)
    # Reverse the remaining n - k elements
    reverse(nums, k, n - 1)

def reverse(arr, start, end):
    """Helper function to reverse elements in the array from start to end indices."""
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]  # Swap elements
        start += 1
        end -= 1

# Example usage:
input_array = [1, 2, 3, 4, 5, 6, 7]
k = 3
rotate_array(input_array, k)
print(f"The rotated array is: {input_array}")  # Output: The rotated array is: [5, 6, 7, 1, 2, 3, 4].