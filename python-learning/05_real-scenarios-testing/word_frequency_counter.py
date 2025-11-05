"""
Problem Statement:
------------------
Write a function that takes a paragraph of text and returns the
top 3 most frequent words (ignore case and punctuation).

What it tests:
--------------
- String processing and cleanup.
- Dictionary-based counting.
- Sorting by value.
"""

def top_three_words(text: str):
    """Return top 3 most frequent words in the text."""
    # Clean text
    for ch in ".,!?;:":
        text = text.replace(ch, "")
    text = text.lower().split()

    word_count = {}
    for word in text:
        word_count[word] = word_count.get(word, 0) + 1

    # Sort by frequency (descending)
    sorted_words = sorted(word_count.items(), key=lambda x: x[1], reverse=True)
    return [word for word, _ in sorted_words[:3]]


# Example usage
if __name__ == "__main__":
    para = "Hello world! Hello Python, Python is great. World of Python."
    print(top_three_words(para))  # Output: ['python', 'hello', 'world']
