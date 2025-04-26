# Question: Rearrange Array
# Given [2, 0, 4, 0, 3, 0, 5, 0], rearrange it so all even numbers come first and odd numbers come last,
# resulting in [0, 0, 0, 0, 2, 4, 3, 5].

def rearrange_array(arr):
    # Step 1: Initialize two lists to hold evens and odds.
    evens = []
    odds = []

    # Step 2: Iterate through the array and categorize numbers.
    for num in arr:
        if num % 2 == 0:  # Check if the number is even.
            evens.append(num)
        else:  # The number is odd.
            odds.append(num)

    # Step 3: Combine the even and odd lists.
    rearranged_array = evens + odds

    # Step 4: Return the rearranged array.
    return rearranged_array

# Example usage
input_array = [2, 0, 4, 0, 3, 0, 5, 0]
result = rearrange_array(input_array)
print(result)  # This should output [2, 0, 4, 0, 0, 3, 5]