# Question: Solve the Two Sum problem using a HashMap for O(n) lookup.

def two_sum(nums, target):
    """Find indices of the two numbers such that they add up to the target using a HashMap."""
    num_map = {}  # HashMap to store the numbers and their indices

    for index, num in enumerate(nums):
        complement = target - num  # Find the complement that, along with num, adds up to target
        if complement in num_map:
            return [num_map[complement], index]  # Return indices of the two numbers
        num_map[num] = index  # Store the index of the current number

    return []  # Return an empty list if no solution is found


# Example usage:
nums = [2, 7, 11, 15]
target = 9
result = two_sum(nums, target)
print(
    f"The indices of the two numbers that add up to {target} are: {result}")  # Output: The indices of the two numbers that add up to 9 are: [0, 1].