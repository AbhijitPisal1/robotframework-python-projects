# Question: Reverse an Array
# Write a program to reverse the elements of an array without using an additional array.

def reverse_array(arr):
    # Step 1: Initialize pointers for left and right ends of the array.
    left = 0
    right = len(arr) - 1

    # Step 2: Swap elements until the pointers meet in the middle.
    while left < right:
        # Step 3: Swap the elements at the left and right pointers.
        arr[left], arr[right] = arr[right], arr[left]
        # Step 4: Move the pointers towards the center.
        left += 1
        right -= 1

    # Step 5: The array is now reversed in place.
    return arr

# Example usage
input_array = [1, 2, 3, 4, 5]
result = reverse_array(input_array)
print(result)  # This should output [5, 4, 3, 2, 1]