# TUPLE COLLECTION DATA TYPE IN PYTHON

"""
A tuple is a built-in collection data type in Python used to store **ordered**, **immutable** elements.
- Syntax: Enclosed in parentheses (), e.g., (1, "text", 3.5)
- Ordered: Maintains the insertion order
- Immutable: Cannot be modified (no adding/removing/replacing elements)
- Indexed: Elements can be accessed via zero-based indexing
- Heterogeneous: Can store values of different data types
- comparable and hashable
- Useful for fixed data collections and safer alternatives to lists
- Tuple vs List
    Tuples are generally used for heterogeneous data (different data types), while lists are preferred for homogeneous data (similar data types).
    Iterating over a tuple is typically faster than iterating over a list, due to the tuple’s immutability.
    Tuples that contain only immutable elements can be used as keys in a dictionary.
    If data should remain constant, using a tuple ensures it is write-protected, as tuples are immutable.
"""
# ========== CREATING A TUPLE ==========
tuple1= 'a', 'b', 'c', 'd'
print(tuple1)   #prints ('a', 'b', 'c', 'd')

tuple2 = tuple('abcde')
print(tuple2)   # prints ('a', 'b', 'c', 'd', 'e')

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

slice_tuple2 = new_tuple[:3]    # Returns (1, 10, 'hundred')
print("Sliced tuple from beginning till index 3:", slice_tuple2)

# ========== CONCATENATING TUPLES ==========
tuple1 = (1, 2)
tuple2 = (3, 4)
concatenated = tuple1 + tuple2
print("Concatenated tuple:", concatenated)

multiplied = tuple1 * 4
print("New Tuple with values repeated 4 times:", multiplied)

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

# ============== TRAVERSE and SEARCH THROUGH A TUPLE ===========
myTuple = ('a', 'b', 'c', 'd', 'e')
for i in range(len(myTuple)):
    print(myTuple[i])

def searchTuple(p_tuple, val):
    for i in range(0, len(p_tuple)):
        if p_tuple[i] == val:
            return f"the {val} element is found at {i} index"
    return "The element is not found"
print(searchTuple(myTuple,'c'))