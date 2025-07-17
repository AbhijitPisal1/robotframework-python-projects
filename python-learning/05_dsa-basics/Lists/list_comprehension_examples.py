"""
List Comprehension in Python
"""
# --------------------------------
# Creating a new list using a for loop
# --------------------------------

prev_list = [1, 2, 3]
new_list = []
for i in prev_list:
    multiply_2 = i * 2
    new_list.append(multiply_2)

print("Using for loop:", new_list)

# --------------------------------
# Using list comprehension (shorter syntax)
# --------------------------------

new_list2 = [i * 2 for i in prev_list]
print("Using list comprehension:", new_list2)

# --------------------------------
# List comprehension from a string (character extraction)
# --------------------------------

lang = 'python'
new_list3 = [letter for letter in lang]
print("Characters in string:", new_list3)

# --------------------------------
# Filtering list: extracting positive numbers
# --------------------------------

numbers = [-1, 2, -3, 4, -5, 6]
positiveNumList = [num for num in numbers if num > 0]
print("Positive numbers:", positiveNumList)

# Filtering and transforming: square negative numbers
NegativeNumList = [num * num for num in numbers if num < 0]
print("Squares of negative numbers:", NegativeNumList)

# --------------------------------
# Filtering consonants from a sentence
# --------------------------------

sentence = "This is a new line"

def is_consonant(letter):
    vowels = 'aeiou'
    return letter.isalpha() and letter.lower() not in vowels

consonants = [i for i in sentence if is_consonant(i)]
print("Consonants in sentence:", consonants)

# --------------------------------
# Conditional expression inside list comprehension
# --------------------------------

new_list4 = [num if num > 0 else 'Negative number' for num in numbers]
print("Replace negatives with label:", new_list4)
