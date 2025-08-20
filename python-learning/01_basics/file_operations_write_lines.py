# This script reads the content of a file, reverses the order of the lines,
# and writes them back to the same file.

# -------------------------------
# Using 'with open(...)' ensures that the file is automatically closed
# after the block is executed, even if an error occurs.
# This is preferred over manually calling file.close().
#
# Open the file in read mode ('r') to read its contents
with open('test.txt', 'r') as reader:
    # Read all lines into a list
    # Each line becomes an element in the list
    reader = reader.readlines()

    # Reversing the order of lines
    # This does not modify the file yet, just the list in memory
    # Useful in scenarios like log analysis, stack-style undo features, etc.
    reversed_lines = reversed(reader)

    # Open the same file in write mode ('w')
    # This clears the file content before writing
    with open('test.txt', 'w') as writer:
        # Write each reversed line back to the file
        # This effectively rewrites the file in reverse line order
        for line in reversed_lines:
            writer.write(line)
