"""
Handle Tuple modification exception with Try Catch
Create a tuple named person that contains three elements: a name (string), an age (integer), and a height (float) with the below values.
"Mark", 25, 5.9
Print the second element of the tuple.
Attempt to change the name in the tuple to a different name and explain why this will or will not work.
"""
person = ("Mark", 25, 5.9)
# Print the second element of the tuple
print(f"Age: {person[1]}")

# Attempt to change the name in the tuple (this will raise an error)
try:
    person[0] = "John"  # This will not work
except Exception as e:
    print(f"Error: {e} - Tuples are immutable.")
