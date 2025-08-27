def remove_vowels_from_sentence(sentence):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    words = sentence.split()  # split sentence into words
    result_words = []

    for word in words:
        new_word = ""
        for char in word.lower():
            if char not in vowels:
                new_word += char
        result_words.append(new_word)

    return " ".join(result_words)

print(remove_vowels_from_sentence("This is a simple sentence"))
# Output: "ths s  smpl sntnc"

def remove_vowels_from_word(word):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    result = ""
    for char in word.lower():
        if char not in vowels:
            result += char
    return result
print(remove_vowels_from_word("apple"))
# Output: ppl