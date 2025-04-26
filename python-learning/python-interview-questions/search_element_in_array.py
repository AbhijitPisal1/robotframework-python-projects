# Question: Search an Element
# Write a program to search for an element in an array and return its index.
# If the element is not found, display a message.

def search_element(array, target):
    # Step 1: Iterate through the array to search for the target element.
    for index, element in enumerate(array):
        # Step 2: Check if the current element matches the target.
        if element == target:
            # Step 3: If found, return the index.
            return index

    # Step 4: If not found, return a message.
    return "Element not found in the array."

# Example usage
input_array = [10, 20, 30, 40, 50]
target_element = 30
result = search_element(input_array, target_element)
print(result)  # This should output 2 (the index of element 30)

# Test case where the element is not found
target_element_not_found = 60
result_not_found = search_element(input_array, target_element_not_found)
print(result_not_found)  # This should output "Element not found in the array."