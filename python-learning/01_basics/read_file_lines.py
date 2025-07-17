# Open the file in read mode
file = open("test.txt")

# -------------------------------
# Method: read()
# Description:
# Reads the entire content of the file as a single string.
# Use Case:
# Useful when we want to process the whole content at once (e.g., small config files, templates).
# Not ideal for large files — it may consume a lot of memory.
# print(file.read())

# -------------------------------
# Method: read(n)
# Description:
# Reads the first 'n' characters from the file.
# Use Case:
# Useful for reading fixed-length headers or previews, or processing data in chunks (e.g., streaming logs).
# print(file.read(2))

# -------------------------------
# Method: readline()
# Description:
# Reads one line at a time from the file.
# Each call to readline() moves the read cursor to the next line.
# Use Case:
# Preferred when processing logs or large files line by line, reducing memory usage.
# print(file.readline())

# -------------------------------
# Example: Reading file line by line using readline()
# Description:
# Reads and prints one line at a time using a loop.
# Use Case:
# Ideal for streaming and analyzing large text files (e.g., log files), where efficiency matters.
# line = file.readline()
# while line != "":
#     print(line)
#     line = file.readline()

# -------------------------------
# Method: readlines()
# Description:
# Reads all lines into a list, where each line is a string item.
# Use Case:
# Useful when we need to manipulate lines as list elements (e.g., sorting, filtering).
# Should be avoided for very large files as it loads all data into memory.
for line in file.readlines():
    print(line)

# Always close the file after reading/writing
# Prevents memory leaks and locks on the file
file.close()
