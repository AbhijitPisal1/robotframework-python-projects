# EXAMPLES OF STRING DATA TYPES
print("EXAMPLES OF STRING DATA TYPES")

# A string is a sequence of characters. Python supports Unicode characters.
# Generally, strings are represented by either single or double quotes.

# Creating strings using double and single quotes
a = "string in a double quote"
b = 'string in a single quote'

# Printing the strings
print("String A:", a)
print("String B:", b)

# Printing particular value for string
print(a[1])     # t

# Using ',' to concatenate the two strings
print("Using comma to concatenate:", a, "concatenated with", b)

# Using '+' to concatenate the two strings
print("Using plus to concatenate:", a + " concatenated with " + b)

# Accessing characters in a string by index
print("First character of string A:", a[0])  # Output: 's'
print("Last character of string B:", b[-1])  # Output: 'e'

# Extracting/Slicing a string
substring = a[0:6]  # Getting substring from index 0 to 5
print("Substring of A (0 to 5):", substring)  # Output: 'string'

# Finding length of a string
length_of_a = len(a)
print("Length of string A:", length_of_a)

# Converting to upper and lower case
print("String A in upper case:", a.upper())  # Output: 'STRING IN A DOUBLE QUOTE'
print("String B in lower case:", b.lower())  # Output: 'string in a single quote'

# Checking if a substring exists within a string
contains_test = "double" in a  # Checks if 'double' is in string A
print("Does string A contain 'double'? :", contains_test)  # Output: True

# Replacing a substring
replaced_string = a.replace("double", "single")
print("String A after replacement:", replaced_string)  # Output: 'string in a single quote'

str2 = "testing"
str3 = "test"
str4 =  "TEST"
print(str3 in str2)
print(str4 in str2)     # case sensitive hence False

str5= "google.com"
var1 = str5.split(".")      # creates a list after splitting string
print(var1)
print(var1[0])      # should print google

str6= "greet "
print(str6.strip())     # removes all whitespaces

str7 = "   leftStrip   "
print((str7.lstrip()))      # removes left side whitespaces i.e beginning whitespace

str8 = " RightStrip  "
print((str8.rstrip()))      # removes right side whitespaces only