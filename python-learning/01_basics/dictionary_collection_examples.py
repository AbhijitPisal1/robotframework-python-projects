# DICTIONARY (dict) COLLECTION DATA TYPE IN PYTHON

"""
A dictionary is a built-in data type in Python used to store key-value pairs.
- Syntax: Enclosed in curly braces {}, e.g., {"name": "Alice", "age": 25}
- Ordered (since Python 3.7+): Maintains insertion order
- Mutable: Can add, modify, or delete items
- Key-based Access: Values accessed using keys, not indexes
- Heterogeneous: Keys and values can be of different types
- Similar to hash tables in other languages
"""

# ========== INITIALIZING A DICTIONARY ==========
dict1 = {1: "first value", "two": 2, "third_key": "This is a dictionary"}
print("Initial dictionary:", dict1)

# ========== ACCESSING VALUES ==========
print("Access using key 1:", dict1[1])  # Output: first value
print("Access using key 'third_key':", dict1["third_key"])  # Output: This is a dictionary

# ========== DISPLAYING KEYS, VALUES, ITEMS ==========
print("Keys:", dict1.keys())      # Returns a view object of keys
print("Values:", dict1.values())  # Returns a view object of values
print("Items:", dict1.items())    # Returns a view object of key-value pairs

# ========== ADDING NEW KEY-VALUE PAIR ==========
dict1["fourth"] = "new value"
print("After adding a new key-value pair:", dict1)

# ========== MODIFYING EXISTING VALUE ==========
dict1[1] = "updated first value"
print("After updating key 1:", dict1)

# ========== DELETING ITEMS ==========
del dict1["two"]  # Deletes key "two"
print("After deleting key 'two':", dict1)

removed_value = dict1.pop("third_key")  # Removes and returns value of "third_key"
print("Removed value using pop():", removed_value)
print("After popping 'third_key':", dict1)

# ========== LOOPING THROUGH DICTIONARY ==========
print("Looping through keys:")
for key in dict1:
    print(key)

print("Looping through values:")
for value in dict1.values():
    print(value)

print("Looping through items:")
for key, value in dict1.items():
    print(f"{key}: {value}")

# ========== CLEARING A DICTIONARY ==========
dict1.clear()
print("After clearing dict1:", dict1)  # Output: {}

# ========== MERGING DICTIONARIES ==========
# Create a new dictionary and merge into dict1
dict2 = {3: "third value", "five": 5}
dict1.update(dict2)
print("After merging dict2 into dict1:", dict1)

# ========== MORE DICTIONARY EXAMPLES ==========
# Another example to reinforce concepts
dict3 = {}  # Empty dictionary

dict3["Country"] = "India"
dict3["Capital"] = "Delhi"

print("New dictionary dict3:", dict3)
print("Accessing 'Capital' from dict3:", dict3["Capital"])
