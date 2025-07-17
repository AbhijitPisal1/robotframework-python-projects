python
"""This function accepts an integer "end" and counts by 10 
from 0 to the "end" value."""


def count_by_10(end):
    """Initialize "count" as an empty string."""
    count = ""

    """The range starts at 0, goes to "end" (inclusive), and 
    increments by 10."""
    for number in range(0, end + 1, 10):
        """Convert each number to a string and append it to 
        "count" with a space for separation."""
        count += str(number) + " "

    """Trim the trailing space from the string "count" before returning."""
    return count.strip()


# Call the function with 1 integer parameter.
print(count_by_10(100))
# Should print 0 10 20 30 40 50 60 70 80 90 100


'''
Created on Jul 18, 2023

@author: APisal
'''