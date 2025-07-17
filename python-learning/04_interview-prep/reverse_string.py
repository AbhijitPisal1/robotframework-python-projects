# Question: Reverse a String using Two-pointer Approach
def reverse_string(s):
    # Convert the string to a list to allow modification
    s_list = list(s)
    left, right = 0, len(s_list) - 1

    # Swap characters until the pointers meet
    while left < right:
        # Swap the characters
        s_list[left], s_list[right] = s_list[right], s_list[left]
        left += 1
        right -= 1

    # Convert the list back to a string
    return ''.join(s_list)


# Example usage
input_string = "hello"
reversed_string = reverse_string(input_string)
print(f"Reversed string: {reversed_string}")  # This should output 'olleh'