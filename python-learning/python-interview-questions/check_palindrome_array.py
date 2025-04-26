# Question: Check Palindrome Array
# Write a program to check if an array is a palindrome.

def is_palindrome_array(array):
    # Step 1: Compare the array with its reverse
    return array == array[::-1]

# Example usage
input_array = [1, 2, 3, 2, 1]
is_palindrome = is_palindrome_array(input_array)

print(f"Is the array a palindrome? {is_palindrome}")  # This should output True