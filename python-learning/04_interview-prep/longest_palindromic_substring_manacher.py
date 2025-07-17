# Question: Find the longest palindromic substring in a given string using Manacher's Algorithm.

def longest_palindromic_substring(s):
    """Find the longest palindromic substring using Manacher’s algorithm."""
    # Preprocess the string to avoid even-length palindrome issues
    T = '#'.join(f'^{s}$')  # Add boundaries and separators
    n = len(T)
    P = [0] * n  # Array to hold the radius of palindromes
    center = right = 0  # Current center and right edge of the rightmost palindrome

    for i in range(1, n - 1):
        mirror = 2 * center - i  # Get the mirror index of i
        if right > i:
            P[i] = min(right - i, P[mirror])  # Use previously computed palindrome lengths

        # Attempt to expand the palindrome centered at i
        while T[i + P[i] + 1] == T[i - P[i] - 1]:
            P[i] += 1

        # Update the center and right boundary if we expanded past the right edge
        if i + P[i] > right:
            center = i
            right = i + P[i]

    # Find the maximum length palindrome in the P array
    max_length = max(P)
    center_index = P.index(max_length)

    # Extract the longest palindromic substring from the original string
    start = (center_index - max_length) // 2  # Adjust index for the original string
    return s[start:start + max_length]


# Example usage:
input_string = "babad"
result = longest_palindromic_substring(input_string)
print(f"The longest palindromic substring in '{input_string}' is: '{result}'")  # Example output: 'bab' or 'aba'.