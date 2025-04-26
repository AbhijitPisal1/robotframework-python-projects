# Let's use tuples to store information about a file:
# its name, its type, and its size in bytes. Fill in the gaps 
# in this code to return the size in kilobytes (1 kilobyte is 
# 1024 bytes) formatted to 2 decimal places.

def file_size(file_info):
    name, type, size = file_info
    return("{:.2f}".format(size / 1024))  # Corrected to use 'size' instead of 'file_info'

print(file_size(('Class Assignment', 'docx', 17875))) # Expected output: 17.46
print(file_size(('Notes', 'txt', 496))) # Expected output: 0.48
print(file_size(('Program', 'py', 1239))) # Expected output: 1.21


'''
Created on Jul 18, 2023

@author: APisal
'''