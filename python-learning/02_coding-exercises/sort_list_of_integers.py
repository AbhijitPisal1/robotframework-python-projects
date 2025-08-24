# Question: Sort integers in descending order
# Input: [10, 14, 29, 23, 24, 15, 13]
# Output: [29, 24, 23, 15, 14, 13, 10]

"""
Approach
implement **insertion sort**, which builds the sorted list one element at a time.
In the descending version of insertion sort:
- We iterate through the list starting from the second element.
- For each element, we compare it with previous elements and shift them to the right if they are smaller.
- We insert the current element into the correct position such that the list remains sorted in descending order.

Time Complexity: O(n^2) in the worst case (for insertion sort)
Space Complexity: O(1) – In-place sorting using constant extra space
"""

def sort_descending(arr):
    # Insertion sort in descending order
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] < key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

# Test Case
test_input = [10, 14, 29, 23, 24, 15, 13]
result = sort_descending(test_input)
print("Output:", result)  # Expected: [29, 24, 23, 15, 14, 13, 10]

"""
NOTE:
To sort in ascending order instead of descending using the first function (insertion sort),
just change this line:
    while j >= 0 and arr[j] < key:
to:
    while j >= 0 and arr[j] > key:
This reverses the comparison logic and results in an ascending sort.
"""


"""
Alternatively, To sort an already sorted Ascending list of integers to descending order i.e. Reverse an Already sorted ascending list
# Input: [10, 13, 14, 15, 23, 24, 29]
# Output: [29, 20, 23, 15, 17, 13, 10]

Approach:
We'll use a simple two-pointer approach: one starting at the beginning, one at the end.
Swap the elements until the pointers meet in the middle.
This ensures in-place reversal of the list without using Python shortcuts like reversed() or slicing.

Note:
    This approach only works correctly if the input list is already sorted in ascending order.
    If the input list is not sorted, simply reversing it will not sort the list in descending order.
    Therefore, this method is not a general solution for sorting but an optimization when the input list is guaranteed to be sorted ascending.
"""

def reverse_list_asc_to_desc(nums):
    left = 0
    right = len(nums) - 1

    while left < right:
        # Swap elements at left and right
        temp = nums[left]
        nums[left] = nums[right]
        nums[right] = temp
        left += 1
        right -= 1

    return nums

# Time Complexity: O(n) where n is the number of elements in the list
# Space Complexity: O(1) as we are modifying the list in-place

# Test case
test_input2 = [10, 13, 14, 15, 23, 24, 29]
result2 = reverse_list_asc_to_desc(test_input2)
print("Output:", result2)  # Output: [29, 24, 23, 15, 17, 13, 10]