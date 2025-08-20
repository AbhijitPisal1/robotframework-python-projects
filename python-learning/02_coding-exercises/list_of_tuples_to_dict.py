# Problem:
# Convert list of tuples to dict
#
# Given a list of tuples where each tuple contains exactly two elements,
# convert this list into a dictionary such that the first element of
# each tuple is the key and the second element is the corresponding value.
#
# Input: [(1, 'a'), (2, 'b')]
# Output: {1: 'a', 2: 'b'}

# -------------------------------------------------------
# Explanation of the Logic:
# 1. Initialize an empty dictionary.
# 2. Iterate over each tuple in the list.
# 3. Extract the first element of the tuple as the key,
#    and the second element as the value.
# 4. Insert the key-value pair into the dictionary.
# 5. Return the populated dictionary.
#
# This method assumes all tuples have exactly two elements.
# -------------------------------------------------------

def list_of_tuples_to_dict(tuples_list):
    result = {}
    for tup in tuples_list:
        # Unpack tuple elements
        key = tup[0]
        value = tup[1]
        # Insert into dictionary
        result[key] = value
    return result

# -------------------------------------------------------
# Time Complexity: O(n), where n is the number of tuples
# Space Complexity: O(n) for the output dictionary
# -------------------------------------------------------

# Test Case
test_input = [(1, 'a'), (2, 'b')]
expected_output = {1: 'a', 2: 'b'}

output = list_of_tuples_to_dict(test_input)

print("Input:           ", test_input)
print("Expected Output: ", expected_output)
print("Actual Output:   ", output)
