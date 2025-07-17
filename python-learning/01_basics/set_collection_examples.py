# SET COLLECTION DATA TYPE IN PYTHON

"""
A set is a built-in collection data type in Python used to store **unique**, **unordered** elements.
- Syntax: Enclosed in curly braces {} or created using the set() constructor
- Unordered: Elements are not stored in any particular order
- Mutable: Elements can be added or removed
- Heterogeneous: Can store different data types (int, str, float, etc.)
- Unique Elements: Duplicates are automatically removed
- Useful for set operations like union, intersection, difference
"""

# ========== INITIALIZING A SET ==========
values = {1, 2, "mark", 4, 5, "mark"}  # Duplicate "mark" will be removed automatically
print("Initial set (duplicates removed):", values)

# ========== ADDING ELEMENTS ==========
values.add("new Object")  # Adds a new item to the set
print("After adding 'new Object':", values)

# ========== REMOVING ELEMENTS ==========
# remove() - removes a specific item, raises KeyError if item is not found
values.remove(2)
print("After removing 2 using remove():", values)

# discard() - removes item if found, does nothing if not found (safe)
values.discard(5)
print("After discarding 5 using discard():", values)

values.discard(100)  # 100 is not present — no error raised
print("After attempting to discard non-existent 100:", values)

# ========== SET OPERATIONS ==========
other_set = {4, 5, 6, 7}
print("Other set:", other_set)

# UNION - combines all unique elements from both sets
union_set = values.union(other_set)
print("Union of values and other_set:", union_set)

# INTERSECTION - elements common to both sets
intersection_set = values.intersection(other_set)
print("Intersection of values and other_set:", intersection_set)

# DIFFERENCE - elements in `values` but not in `other_set`
difference_set = values.difference(other_set)
print("Difference of values - other_set:", difference_set)
