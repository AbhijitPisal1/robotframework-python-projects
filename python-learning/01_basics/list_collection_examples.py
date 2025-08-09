# LIST COLLECTION DATA TYPE IN PYTHON

"""
A list is a built-in collection type in Python used to store multiple values.
- Syntax: Enclosed in square brackets [], e.g., [1, "apple", 3.14]
- Ordered: Maintains insertion order
- Mutable: Can add, remove, or modify items
- Indexed: Supports positive and negative indexing, slicing
- Heterogeneous: Can contain different data types (int, str, float, etc.)
- Allows duplicates: Elements can appear more than once
"""

# ========== DECLARING A LIST ==========
custom = [1, 2, "test", 4, 5, 2, "test"]
print("Initial list:", custom)

# ========== ACCESSING ELEMENTS ==========
print("First element (index 0):", custom[0])
print("Last element (index -1):", custom[-1])
print("Slice from index 1 to 3:", custom[1:4])  # [2, 'test', 4]

# ========== MODIFYING THE LIST ==========

# Inserting an element at a specific index
custom.insert(3, "inserted")  # Inserts at index 3
print("After insert at index 3:", custom)

# Appending an element at the end
custom.append("end")
print("After appending 'end':", custom)

# Updating an element at a specific index
custom[2] = "TEST"  # Replace "test" with "TEST"
print("After updating index 2:", custom)

# Deleting an element by index
del custom[0]
print("After deleting element at index 0:", custom)

# Popping (removing and returning) the last element or element at the given index
popped_item = custom.pop()
print("Popped item:", popped_item)
print("After pop():", custom)

# Removing a specific value (first occurrence only)
custom.remove("test")
print("After removing 'test':", custom)

# ========== SEARCHING AND COUNTING ==========
# Finding the index of the first occurrence of 4
index_of_4 = custom.index(4)
print("Index of 4:", index_of_4)

# Counting occurrences of the number 2
count_2 = custom.count(2)
print("Count of 2:", count_2)

# ========== OTHER LIST OPERATIONS ==========

# Getting the number of elements
length = len(custom)
print("Length of list:", length)

# Reversing the list in place
custom.reverse()
print("After reversing:", custom)

# ========== FINAL STATE ==========
print("Final list:", custom)