# Question: Write a program to find duplicate elements in a string array.

def find_duplicates(string_array):
    # Step 1: Initialize a set to keep track of seen elements and a list for duplicates.
    seen = set()
    duplicates = []

    # Step 2: Iterate through each string in the array.
    for string in string_array:
        # Step 3: Check if the string has been seen before.
        if string in seen:
            # Step 4: If seen, it's a duplicate; add it to the duplicates list if not already added.
            if string not in duplicates:
                duplicates.append(string)
        else:
            # Step 5: Otherwise, add it to the seen set.
            seen.add(string)

    # Step 6: Return the list of duplicates.
    return duplicates

# Example usage
input_array = ["apple", "banana", "apple", "orange", "banana", "grape"]
result = find_duplicates(input_array)
print(result)  # This should output ['apple', 'banana']