# Question: Count Even and Odd Numbers
# Write a program to count the number of even and odd numbers in an array of integers.

def count_even_odd(int_array):
    # Step 1: Initialize counters for even and odd numbers.
    even_count = 0
    odd_count = 0

    # Step 2: Iterate through each integer in the array.
    for num in int_array:
        # Step 3: Check if the number is even or odd and update the counters.
        if num % 2 == 0:  # Even
            even_count += 1
        else:             # Odd
            odd_count += 1

    # Step 4: Return the counts of even and odd numbers.
    return even_count, odd_count

# Example usage
input_array = [1, 2, 3, 4, 5, 6, 7, 8]
even_result, odd_result = count_even_odd(input_array)
print(f"Even Count: {even_result}, Odd Count: {odd_result}")  # This should output Even Count: 4, Odd Count: 4