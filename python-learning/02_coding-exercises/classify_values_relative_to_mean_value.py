# Problem:
# 17. Values greater, equal, and lesser than average from int array
# Given an integer array, find the average and return three lists containing values greater than,
# equal to, and lesser than the average respectively.
# Input: [10, 20, 30, 40, 50] → avg = 30
# Output: Greater: [40, 50], Equal: [30], Lesser: [10, 20]
"""
Approach:
First, calculate the average by summing all elements and dividing by the number of elements.
Then iterate through the array and compare each element with the average.
Append elements to corresponding lists for greater than, equal to, or less than the average.
Return all three lists.
This requires two passes over the data: one for average calculation and one for classification.
"""
def classify_by_average(arr):
    if len(arr) == 0:
        return [], [], []  # Handle empty input by returning empty lists

    total = 0
    count = 0
    for num in arr:
        total += num
        count += 1
    average = total / count

    greater = []
    equal = []
    lesser = []

    for num in arr:
        if num > average:
            greater.append(num)
        elif num == average:
            equal.append(num)
        else:
            lesser.append(num)

    return greater, equal, lesser

# Time Complexity: O(n) where n is the number of elements in the array
# Space Complexity: O(n) for storing the three separate lists

# Test case
test_arr = [10, 20, 30, 40, 50]
g, e, l = classify_by_average(test_arr)
print("Greater:", g)  # Output: [40, 50]
print("Equal:", e)    # Output: [30]
print("Lesser:", l)   # Output: [10, 20]