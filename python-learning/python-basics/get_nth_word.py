# Complete the get_word function using the "split" method to return the {n}th word from a sentence.
# For instance, get_word("This is a lesson about lists", 4) should return "lesson", the 4th word.
# Note: List indexes start at 0, not 1.

def get_word(sentence, n):
    # Proceed only if n is positive.
    if n > 0:
        words = sentence.split()
        # Proceed only if n does not exceed the word count.
        if n <= len(words):
            return words[n - 1]  # Adjust index for 0-based counting.


print(get_word("This is a lesson about lists", 4))  # Should print: lesson
print(get_word("This is a lesson about lists", -4))  # Nothing
print(get_word("Now we are cooking!", 1))  # Should print: Now
print(get_word("Now we are cooking!", 5))  # Nothing

'''
Created on Jul 18, 2023

@author: APisal
'''