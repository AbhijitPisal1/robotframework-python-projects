# Question: Increment a Number Represented as an Array
# Consider an array like [1, 2, 9], which represents the number 129.
# When you add one, the result should be [1, 3, 0].
# Similarly, [9, 9, 9] should become [1, 0, 0, 0].

def increment_array(arr):
    # Step 1: Start from the last digit and initialize carry to 1 (for the increment).
    carry = 1

    # Step 2: Iterate over the array in reverse order.
    for i in range(len(arr) - 1, -1, -1):
        # Step 3: Add the carry to the current digit.
        new_value = arr[i] + carry
        # Step 4: Update the current digit and calculate the carry for the next iteration.
        if new_value < 10:
            arr[i] = new_value
            carry = 0
            break
        else:
            arr[i] = 0
            carry = 1

    # Step 5: If there's still a carry after processing all digits, insert it at the front.
    if carry:
        arr.insert(0, 1)

    # Step 6: Return the modified array.
    return arr


# Example usage
input_array1 = [1, 2, 9]
result1 = increment_array(input_array1)
print(result1)  # This should output [1, 3, 0]

input_array2 = [9, 9, 9]
result2 = increment_array(input_array2)
print(result2)  # This should output [1, 0, 0, 0]