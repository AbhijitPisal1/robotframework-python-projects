def is_palindrome(s):
    """Check if the input string is a palindrome."""
    s = s.lower().replace(" ", "")  # Normalize the string
    return s == s[::-1]  # Check if the string is equal to its reverse

# Example usage:
test_string = "A man a plan a canal Panama"
result = is_palindrome(test_string)
print(f"Is '{test_string}' a palindrome? {result}")  # Output: True