# Question: Find Maximum and Minimum
# Write a program to find the maximum and minimum values in an array of integers.

def find_max_min(int_array):
    # Step 1: Check if the array is empty.
    if not int_array:
        return None, None  # Return None for both max and min if the array is empty.

    # Step 2: Initialize max and min with the first element of the array.
    max_value = int_array[0]
    min_value = int_array[0]

    # Step 3: Iterate through each integer in the array.
    for num in int_array:
        # Step 4: Update max_value if the current number is greater.
        if num > max_value:
            max_value = num
        # Step 5: Update min_value if the current number is smaller.
        if num < min_value:
            min_value = num

    # Step 6: Return the found maximum and minimum values.
    return max_value, min_value


# Example usage
input_array = [5, 1, 3, 9, 2, -4]
max_result, min_result = find_max_min(input_array)
print(f"Maximum: {max_result}, Minimum: {min_result}")  # This should output Maximum: 9, Minimum: -4

"""Alternatively, Find the maximum and minimum values in an array using built-in functions.
def find_max_min(int_array):
    
    if not int_array:
        return None, None  # Return None for both max and min if the array is empty.

    max_value = max(int_array)  # Use built-in max function
    min_value = min(int_array)  # Use built-in min function

    return max_value, min_value

# Example usage:
input_array = [5, 1, 3, 9, 2, -4]
max_result, min_result = find_max_min(input_array)
print(f"Maximum: {max_result}, Minimum: {min_result}")  # Output: Maximum: 9, Minimum: -4"""
