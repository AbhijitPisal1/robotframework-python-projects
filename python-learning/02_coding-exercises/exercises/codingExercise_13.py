"""
Read and Print File Contents
Objective: Write a program to read the contents of a file and print it to the console.

Instructions:
Sample file file1.txt is provided with this assignment.
Write a Python script that opens the file and reads all its contents.
Print the entire content of the file.
"""

# Open the file in read mode
with open("file1.txt", "r") as file:
    content = file.read()

# Print the contents of the file
print(content)
