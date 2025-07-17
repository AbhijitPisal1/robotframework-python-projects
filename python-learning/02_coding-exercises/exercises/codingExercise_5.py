"""
Understanding Dictionaries
Create a dictionary named car with the following keys: make, model, year, and color.
Assign appropriate values to each key.
    "make": "Toyota",
    "model": "Camry",
    "year": 2020,
    "color": "Blue"
Print the value associated with the model key.
Add a new key called owner and assign it the name "Rahul".
Print the entire dictionary.

Expected Result:
Car model: Camry
Updated car dictionary: {'make': 'Toyota', 'model': 'Camry', 'year': 2020, 'color': 'Blue', 'owner': 'Rahul'}
"""

# Create the dictionary
car = {
    "make": "Toyota",
    "model": "Camry",
    "year": 2020,
    "color": "Blue"
}

# Print the value associated with the model key
print("Car model:", car["model"])

# Add a new key called owner
car["owner"] = "Rahul"

# Print the entire updated dictionary
print("Updated car dictionary:", car)
