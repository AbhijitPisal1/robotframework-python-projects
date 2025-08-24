# Question: Split a string into a list, modifies each element by moving
# its first character to the end, and adds a dash before the moved character. 
# For example, "2two" becomes "two-2". Finally, it converts the list back 
# to a string and returns it.
def change_string(given_string):

# Initializes "new_string" as an empty string.
    new_string = ""
    # Splits "given_string" into "new_list", where each "element" contains
    # an individual word from the string.
    new_list = given_string.split()

    # Iterates over each "element" in "new_list".
    for element in new_list:

        # Concatenates to form "new_string" by combining: 
        # + The substring from the second character onward ([1:]), 
        # + a dash "-",
        # + the first character ([0]), 
        # + and a space " " for separation.
        new_string += element[1:] + "-" + element[0] + " "

    # Returns the formed string.
    return new_string


print(change_string("1one 2two 3three 4four 5five")) 
# Expected output: "one-1 two-2 three-3 four-4 five-5"  


'''
Created on Jul 18, 2023

@author: APisal
'''