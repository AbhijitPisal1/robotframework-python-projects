# Problem:
# 35. Find second largest/smallest number in a list
# Avoid using sort() directly

"""
Explanation:
To find the second largest and second smallest numbers without sorting the list,
we can traverse the list once to find the largest and smallest values,
then traverse again to find the second largest and second smallest by ignoring the previously found values.
This approach avoids sorting and uses simple comparisons to track needed values.

Time Complexity: O(n)
Space Complexity: O(1)
"""

def find_second_largest_and_smallest(nums):
    if len(nums) < 2:
        return None, None  # Not enough elements for second largest/smallest

    # Initialize largest and smallest
    largest = smallest = nums[0]
    for num in nums:
        if num > largest:
            largest = num
        if num < smallest:
            smallest = num

    # Initialize second largest and second smallest as None
    second_largest = None
    second_smallest = None

    for num in nums:
        # For second largest, find max number less than largest
        if num != largest:
            if second_largest is None or num > second_largest:
                second_largest = num
        # For second smallest, find min number greater than smallest
        if num != smallest:
            if second_smallest is None or num < second_smallest:
                second_smallest = num

    return second_largest, second_smallest


# Test case
nums = [4, 1, 7, 3, 9, 9, 2]
second_largest, second_smallest = find_second_largest_and_smallest(nums)
print("Second Largest:", second_largest)  # Expected: 7
print("Second Smallest:", second_smallest)  # Expected: 2