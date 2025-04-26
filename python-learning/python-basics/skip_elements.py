# Try out the enumerate function for yourself in this quick exercise.
# Complete the skip_elements function to return every other element from the list,
# using the enumerate function to determine if an element is at an
# even or odd index.

def skip_elements(elements):
    # code goes here
    # element = [e for i, e in enumerate(elements) if i % 2 == 0]
    # return element

    element1 = []
    for i, e in enumerate(elements):
        if i % 2 == 0:
            element1.append(e)
    return element1


print(skip_elements(["a", "b", "c", "d", "e", "f", "g"]))  # Should output ['a', 'c', 'e', 'g']
print(skip_elements(
    ['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach']))  # Should output ['Orange', 'Strawberry', 'Peach']

'''
Created on Jul 18, 2023

@author: APisal
'''