# This code computes the total number of characters in a list of animal names
# and calculates the average length of the names. 
# It also enumerates a list of winners, printing their rank and names.
animals = ['Lion', 'zebra', 'dolphin', 'monkey']
char1 = 0

for animal in animals:
    char1 += len(animal)
print("total characters: {}, Average length: {}".format(char1, char1 / len(animals)))

winners = ['abdc', 'hduhfin', 'skdjj']
for index, person in enumerate(winners):
    print("{}-{}".format(index + 1, person))

'''
Created on Jul 18, 2023

'''