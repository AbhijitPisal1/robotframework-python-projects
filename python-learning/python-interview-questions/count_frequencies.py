# Question: Frequency of Elements
# Write a program to count the frequency of each element in an array.

def count_frequencies(array):
    # Step 1: Create an empty dictionary to hold frequency counts.
    frequency_dict = {}

    # Step 2: Iterate through each element in the array.
    for element in array:
        # Step 3: Update the count in the dictionary.
        if element in frequency_dict:
            frequency_dict[element] += 1  # Increment count if element exists
        else:
            frequency_dict[element] = 1    # Initialize count if element is new

    # Step 4: Return the frequency dictionary.
    return frequency_dict

# Example usage
input_array = [1, 2, 2, 3, 4, 4, 4]
frequency_result = count_frequencies(input_array)

# Format the output
output = ', '.join(f"{key}: {value}" for key, value in frequency_result.items())
print(output)  # This should output "1: 1, 2: 2, 3: 1, 4: 3"