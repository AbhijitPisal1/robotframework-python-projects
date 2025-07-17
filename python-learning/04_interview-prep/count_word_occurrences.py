# Question: Count Word Occurrences in a Sentence
# Given a string like "my name is Rohan Rohan",
# the goal is to print each word along with how many times it appears.

from collections import Counter


def count_word_occurrences(sentence):
    # Step 1: Normalize the sentence to lowercase to ensure case-insensitivity.
    normalized_sentence = sentence.lower()

    # Step 2: Split the sentence into words.
    words = normalized_sentence.split()

    # Step 3: Count occurrences of each word using Counter.
    word_count = Counter(words)

    # Step 4: Print each word and its count.
    for word, count in word_count.items():
        print(f'"{word}" → {count} times')


# Example usage
input_sentence = "my name is Rohan Rohan"
count_word_occurrences(input_sentence)
