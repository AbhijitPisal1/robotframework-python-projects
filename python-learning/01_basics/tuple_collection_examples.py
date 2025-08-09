# TUPLE COLLECTION DATA TYPE IN PYTHON

"""
A tuple is a built-in collection data type in Python used to store **ordered**, **immutable** elements.
- Syntax: Enclosed in parentheses (), e.g., (1, "text", 3.5)
- Ordered: Maintains the insertion order
- Immutable: Cannot be modified (no adding/removing/replacing elements)
- Indexed: Elements can be accessed via zero-based indexing
- Heterogeneous: Can store values of different data types
- Useful for fixed data collections and safer alternatives to lists
"""

# ========== CREATING A TUPLE ==========
new_tuple = (1, 10, "hundred", 1000, 1)
print("New tuple:", new_tuple)

# ========== ACCESSING ELEMENTS ==========
print("Second value (index 1):", new_tuple[1])  # Output: 10

# ========== IMMUTABILITY EXAMPLE ==========
# Attempting to modify a tuple will raise an error
try:
    new_tuple[2] = "HUNDRED"
except Exception as e:
    print(f"Error: {e} - Tuples are immutable.")

# ========== SLICING ==========
slice_tuple = new_tuple[1:3]  # Returns a slice: (10, 'hundred')
print("Sliced tuple [1:3]:", slice_tuple)

# ========== CONCATENATING TUPLES ==========
tuple1 = (1, 2)
tuple2 = (3, 4)
concatenated = tuple1 + tuple2
print("Concatenated tuple:", concatenated)

# ========== COUNTING OCCURRENCES ==========
count_of_one = new_tuple.count(1)  # How many times 1 appears
print("Count of 1 in new_tuple:", count_of_one)

# ========== FINDING INDEX ==========
index_of_hundred = new_tuple.index("hundred")
print("Index of 'hundred':", index_of_hundred)

# ========== LENGTH OF TUPLE ==========
length = len(new_tuple) # Number of elements /entries in a tuple
print("Length of new_tuple:", length)

# ========== REVERSING A TUPLE ==========
reversed_tuple = new_tuple[::-1]  # Returns a new tuple in reverse order
print("Reversed tuple:", reversed_tuple)

# ========== MEMBERSHIP TEST ==========
exists = "hundred" in new_tuple
print("Does 'hundred' exist in new_tuple?", exists)

# ========== SINGLE ELEMENT TUPLE ==========
# Note: A single-element tuple must have a trailing comma
single_element = (5,)
print("Single-element tuple:", single_element)

# ========== TUPLE CONSTRUCTOR ==========
constructed_tuple = tuple((6, 7, 8))  # Using tuple() to construct a tuple
print("Tuple created with constructor:", constructed_tuple)

# ========== WORKING WITH A MIXED DATA TUPLE ==========
person = ("Rahul", 25, 5.9)
print(f"Age from person tuple: {person[1]}")

# Attempt to change value (will raise error due to immutability)
try:
    person[0] = "John"
except Exception as e:
    print(f"Error: {e} - Tuples are immutable.")
