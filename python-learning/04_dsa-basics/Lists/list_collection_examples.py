"""
Lists in Python
"""

# ========== DECLARING A LIST ==========
custom = [1, 2, "check", 4, 5, 2, "test"]
print("Initial list:", custom)

# ========== ACCESSING ELEMENTS ==========
print("First element (index 0):", custom[0])
print("Last element (index -1):", custom[-1])
print("Slice from index 1 to 3:", custom[1:4])  # [2, 'test', 4]

# ========== MODIFYING THE LIST ==========
# Updating an element at a specific index
custom[2] = "CHECK"  # Replace "test" with "TEST"
print("After updating index 2:", custom)

# Inserting an element at a specific index
custom.insert(3, "inserted")  # Inserts at index 3
print("After insert at index 3:", custom)

# Appending an element at the end
custom.append("end")
print("After appending 'end':", custom)

# Extending another list into existing list at end
newList=[11,'test',13, 10.5, "new"]
custom.extend(newList)
print(custom)

# slicing and updating list
custom[0:2]=[ 'a', 5]
print(custom)

# Popping (removing and returning) the last element
popped_item = custom.pop()
print("Popped item:", popped_item)
print("After pop():", custom)

# Popping (removing and returning) the specific element
popped_item = custom.pop(2)
print("Popped item:", popped_item)
print("After pop():", custom)

# Deleting an element by index
del custom[0]
print("After deleting element at index 0:", custom)

# Deleting an element by slicing
del custom[1:3]
print("After deleting elements from sliced list:", custom)

# Removing a specific value (first occurrence only)
custom.remove("test")
print("After removing 'test':", custom)

# ========== SEARCHING AND COUNTING ==========
# Finding the index of the first occurrence of 13
index_of_13 = custom.index(13)
print("Index of 13:", index_of_13)

# Counting occurrences of the number 5
count_5 = custom.count(5)
print("Count of 5:", count_5)

# ========== OTHER LIST OPERATIONS ==========

# Getting the number of elements
length = len(custom)
print("Length of list:", length)

# Reversing the list in place
custom.reverse()
print("After reversing:", custom)

# -------------------------------
# List Concatenation and Repetition
# -------------------------------

a_list = [1, 2, 3]
b_list = [4, 5, 6]
c_list = a_list + b_list  # Concatenates two lists
print("Concatenated list:", c_list)

d_list = [0]
print("Original d_list:", d_list)
d_list = d_list * 4       # Repeats elements 4 times
print("Repeated d_list:", d_list)

e_list = [0, 1]
print("Original e_list:", e_list)
e_list = e_list * 3       # Repeats sequence 3 times
print("Repeated e_list:", e_list)

# -------------------------------
# Basic List Functions
# -------------------------------

f_list = [0, 1, 2, 3, 4, 5, 6]
print("Length of f_list:", len(f_list))
print("Maximum value:", max(f_list))
print("Minimum value:", min(f_list))
print("Sum of elements:", sum(f_list))

average = sum(f_list) / len(f_list)
print("Average of elements:", average)

# -------------------------------
# Strings and List Operations
# -------------------------------

# Convert a string into a list of characters
str1 = 'spam'
list1 = list(str1)
print("Characters in string:", list1)

# Split a sentence into words using whitespace
str2 = 'This is a sentence'
list2 = str2.split()  # Default split by whitespace
print("Words from sentence:", list2)

# Split a domain-like string using a custom delimiter
str3 = "www.google.com"
delimiter = '.'
list3 = str3.split(delimiter)
print("Split by delimiter:", list3)

# Join the list back into a string using the same delimiter
joined_str = delimiter.join(list3)
print("Joined string:", joined_str)

