# Question: Find duplicate characters in a given string

def find_duplicate_characters(input_string):
    # Step 1: Initialize a set to track seen characters and a list for duplicates.
    seen = set()
    duplicates = []
    uniques = []
    # Step 2: Iterate through each character in the string.
    for char in input_string:
        # Step 3: Check if the character has been seen before.
        if char in seen:
            # Step 4: If it's a duplicate and not already added, append to duplicates.
            if char not in duplicates:
                duplicates.append(char)
                if char in uniques:
                    uniques.remove(char)
        else:
            # Step 5: If not seen, add to the seen set.
            seen.add(char)
            uniques.append(char)

    # Step 6: Return the list of duplicate characters.
    return duplicates, uniques

# Example usage
# input_str = "programming"
num = 5236286913732
input_str = str(num)
result = find_duplicate_characters(input_str)
print(result)  # Output should be ['r', 'g', 'm']
