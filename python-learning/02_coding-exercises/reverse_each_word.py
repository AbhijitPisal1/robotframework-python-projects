# Question: Reverse Each Word in a Sentence
# Given "abc de f", reverse each word individually while keeping spaces in place.
# The expected output is "fed cb a".

def reverse_each_word(sentence):
    # Step 1: Split the sentence into words based on spaces.
    words = sentence.split(' ')  # Keep the spaces intact

    # Step 2: Reverse each word individually.
    reversed_words = [word[::-1] for word in words]

    # Step 3: Join the reversed words back into a single string with spaces.
    result = ' '.join(reversed_words)

    # Step 4: Return the final result.
    return result

# Example usage
input_sentence = "abc de f"
result = reverse_each_word(input_sentence)
print(result)  # This should output "fed cb a"


"""
def reverse_each_word(sentence):
    reversed_words = []
    words = sentence.split(' ')
    for word in words:
        reversed_word = ""
        index = len(word) - 1
        while index >= 0:
            reversed_word += word[index]
            index -= 1
        reversed_words.append(reversed_word)

    return reversed_words
"""