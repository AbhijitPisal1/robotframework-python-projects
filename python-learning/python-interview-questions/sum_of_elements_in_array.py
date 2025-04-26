# Question: Sum of Elements
# Write a program to take an array of integers as input and calculate the sum of all elements in the array.

def sum_of_elements(int_array):
    # Step 1: Initialize a variable to hold the sum.
    total_sum = 0

    # Step 2: Iterate through each integer in the array.
    for num in int_array:
        # Step 3: Add each integer to the total sum.
        total_sum += num

    # Step 4: Return the calculated sum.
    return total_sum

# Example usage
input_array = [1, 2, 3, 4, 5]
result = sum_of_elements(input_array)
print(result)  # This should output 15