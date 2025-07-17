# Question: Second Largest Element
# Write a program to find the second largest element in an array.

def find_second_largest(array):
    # Step 1: Check if the array has at least two unique elements.
    unique_elements = list(set(array))  # Remove duplicates

    if len(unique_elements) < 2:
        return "Array must contain at least two unique elements."

    # Step 2: Sort the unique elements in descending order.
    unique_elements.sort(reverse=True)

    # Step 3: The second largest element will be the second element in the sorted list.
    return unique_elements[1]


# Example usage
input_array = [10, 20, 4, 45, 99, 99, 45]
second_largest = find_second_largest(input_array)
print(f"The second largest element is: {second_largest}")  # This should output 45

# Test case where the array doesn't have enough unique elements
input_array_two = [5, 5, 5]
second_largest_two = find_second_largest(input_array_two)
print(second_largest_two)  # This should output "Array must contain at least two unique elements."