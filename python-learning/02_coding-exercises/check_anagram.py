# Question: Check if two strings are anagrams of each other.

def are_anagrams(str1, str2):
    """Check if two strings are anagrams of each other."""
    # Clean the strings: remove spaces, convert to lowercase
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    # Sort and compare the strings
    return sorted(str1) == sorted(str2)


# Example usage:
string1 = "Listen"
string2 = "Silent"
result = are_anagrams(string1, string2)
print(f"'{string1}' and '{string2}' are anagrams: {result}")  # Output: 'Listen' and 'Silent' are anagrams: True.