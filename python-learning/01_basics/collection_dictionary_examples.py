# DICTIONARY (dict) COLLECTION DATA TYPE IN PYTHON

"""
A dictionary is a built-in data type in Python used to store key-value pairs.
- Syntax: Enclosed in curly braces {}, e.g., {"name": "Alice", "age": 25}
- Ordered (since Python 3.7+): Maintains insertion order
- Mutable: Can add, modify, or delete items
- Key-based Access: Values accessed using keys, not indexes
- Heterogeneous: Keys and values can be of different types
- How Dictionaries Work Internally:
    - Python dictionaries use a hash function to convert keys into a number.
    - This number determines the index in an internal array where the key-value pair is stored.
    - When you access the key, Python hashes it again to find the value quickly.
"""

# ========== CREATING DICTIONARIES ==========

# Empty dictionaries
my_dict = dict()
print("Empty dict using dict():", my_dict)

my_dict2 = {}
print("Empty dict using {}:", my_dict2)

# Using keyword arguments
eng_sp = dict(one='uno', two='dos', three='tres')
print("English to Spanish dict:", eng_sp)

# Using curly braces
sp_eng = {'uno': 'one', 'dos': 'two', 'tres': 'three'}
print("Spanish to English dict:", sp_eng)

# Using list of tuples
sp_eng2 = dict([('uno', 'one'), ('dos', 'two'), ('tres', 'three')])
print("Dict from list of tuples:", sp_eng2)

# Another example
dict1 = {1: "first value", "two": 2, "third_key": "This is a dictionary"}
print("Initial dict1:", dict1)

# ========== ACCESSING VALUES ==========

print("Access using key 1:", dict1[1])
print("Access using key 'third_key':", dict1["third_key"])

# Using get (safe access with default)
print("Access using get():", dict1.get("two", "Key not found"))

# ========== DISPLAYING KEYS, VALUES, ITEMS ==========

print("Keys:", dict1.keys())
print("Values:", dict1.values())
print("Items:", dict1.items())

# ========== ADDING & MODIFYING VALUES ==========

dict1["fourth"] = "new value"  # Add
print("After adding 'fourth':", dict1)

dict1[1] = "updated first value"  # Modify
print("After updating key 1:", dict1)

# Another example
user = {'name': 'john', 'age': 26}
print("User dict:", user)
user['age'] = 23
print("Updated age:", user)
user['address'] = 'London'
print("Added address:", user)

# ========== DELETING ITEMS ==========

# Delete using del
del user['age']
print("After del on 'age':", user)

# Delete using pop
removed_value = dict1.pop("third_key", "Not found")
print("Removed using pop():", removed_value)
print("After pop on 'third_key':", dict1)

# Remove last inserted item
removed_item = user.popitem()
print("Removed item using popitem():", removed_item)
print("After popitem:", user)

# Clear dictionary
dict1.clear()
print("After clearing dict1:", dict1)

# ========== LOOPING THROUGH DICTIONARIES ==========

print("Looping through keys:")
for key in sp_eng:
    print(key)

print("Looping through values:")
for value in sp_eng.values():
    print(value)

print("Looping through items:")
for key, value in sp_eng.items():
    print(f"{key}: {value}")

# Function to traverse dictionary
def traverse_dict(d):
    for key in d:
        print(f"{key}: {d[key]}")

print("Traversing user dict:")
traverse_dict(user)

# Function to search dictionary by value
def search_dict(d, value):
    for key in d:
        if d[key] == value:
            return key, value
    return 'The value does not exist'

print("Searching for value 23:", search_dict(user, 23))

# ========== DICTIONARY METHODS ==========

dict2 = {1: 'one', 2: 'two', 3: 'three'}
print("Original dict2:", dict2)

# copy()
dict3 = dict2.copy()
print("Copied dict3:", dict3)

# fromkeys()
dict4 = {}.fromkeys([1, 2, 3], 0)
print("Fromkeys dict4:", dict4)

# get()
print("Get key 1 from dict4:", dict4.get(1))

# items()
print("Items in dict4:", dict4.items())

# keys()
print("Keys in dict4:", dict4.keys())

# setdefault()
print("Using setdefault on 4:", dict4.setdefault(4, 0))
print("After setdefault:", dict4)

# values()
print("Values in dict4:", dict4.values())

# Membership checks
rank = {1: 'one', 3: 'three', 2: 'two', 5: 'five', 4: 'four'}
print("Is key 1 in rank?", 1 in rank)
print("Is value 'two' in rank?", 'two' in rank.values())
print("Length of rank:", len(rank))
print("Sorted keys in rank:", sorted(rank))

# ========== DICTIONARY COMPREHENSIONS ==========

import random

city_names = ['Paris', 'London', 'Rome', 'Berlin', 'Madrid']
city_temps = {city: random.randint(20, 30) for city in city_names}
print("City temperatures:", city_temps)

# Filtering with comprehension
above_25 = {city: temp for city, temp in city_temps.items() if temp > 25}
print("Cities with temp > 25:", above_25)

# ========== MERGING DICTIONARIES ==========

dict_a = {'Country': 'India', 'Capital': 'Delhi'}
dict_b = {3: "third value", "five": 5}

dict_a.update(dict_b)
print("After merging dict_b into dict_a:", dict_a)

# End of merged dictionary demo
