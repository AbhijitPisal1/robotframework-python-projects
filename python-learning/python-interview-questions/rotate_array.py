# Question: Rotate an Array
# Write a program to rotate an array to the right by a given number of steps.

def rotate_array(array, steps):
    # Step 1: Handle empty array or steps equal to 0
    if not array or steps <= 0:
        return array

    # Step 2: Normalize the number of steps (to handle cases where steps > len(array))
    steps = steps % len(array)

    # Step 3: Perform the rotation using slicing
    rotated_array = array[-steps:] + array[:-steps]

    return rotated_array

# Example usage
input_array = [1, 2, 3, 4, 5]
rotate_steps = 2
rotated_result = rotate_array(input_array, rotate_steps)

print(f"Rotated array: {rotated_result}")  # This should output [4, 5, 1, 2, 3]