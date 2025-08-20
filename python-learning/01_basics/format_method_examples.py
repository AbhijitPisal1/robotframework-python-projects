example = "format() method"

formatted_string = "this is an example of using the {} on a string".format(example)

print(formatted_string)

"""Outputs:
this is an example of using the format() method on a string
"""

# "{0} {1}".format(first, second)

first = "apple"
second = "banana"
third = "carrot"

formatted_string = "{0} {2} {1}".format(first, second, third)

print(formatted_string)

"""Outputs:
apple carrot banana
"""


# This function converts weight from ounces to pounds. The output 
# is formatted as, "x ounces equals y pounds," with y rounded to 
# 2 decimal places. 
def convert_weight(ounces):
    # Conversion formula: 1 pound = 16 ounces
    pounds = ounces / 16

    # The result is created using the .format() method. It includes 
    # two placeholders: the first for the "ounces" variable and the 
    # second for the "pounds" variable, formatted to 2 decimal places.
    result = "{} ounces equals {:.2f} pounds".format(ounces, pounds)
    return result


print(convert_weight(12))  # Should output: 12 ounces equals 0.75 pounds
print(convert_weight(50.5))  # Should output: 50.5 ounces equals 3.16 pounds
print(convert_weight(16))  # Should output: 16 ounces equals 1.00 pounds


# This function creates a username from the first 3 letters of
# a user’s last name combined with their birth year. 
def username(last_name, birth_year):
    # The .format() method uses the first 3 letters from the
    # "last_name" variable for the first {} placeholder, 
    # and concatenates the "birth_year" for the second placeholder.
    return ("{}{}".format(last_name[0:3], birth_year))


print(username("Ivanov", "1985"))
# Should display "Iva1985" 
print(username("Rodríguez", "2000"))
# Should display "Rod2000" 
print(username("Deng", "1991"))
# Should display "Den1991"


'''
Created on Jul 18, 2023

@author: APisal
'''