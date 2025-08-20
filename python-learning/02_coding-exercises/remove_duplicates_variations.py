# Problem:
# 22. Remove duplicates from a list (preserve order)
# Given a list, remove all duplicate elements while preserving the original order of first occurrences.
# Example: [3, 5, 3, 2, 5, 1] → [3, 5, 2, 1]

"""
Approach:
Use a set to track elements that have already appeared.
Iterate through the list, and for each element, check if it is in the set:
- If not, add it to the set and append it to the result list.
- If yes, skip it.
This preserves the order of first occurrences and removes duplicates.
"""

def remove_duplicates_preserve_order(lst):
    seen = set()
    result = []
    for item in lst:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

# Time Complexity: O(n) where n is the length of the list
# Space Complexity: O(n) for the set and output list in the worst case

# Test case
test_list = [3, 5, 3, 2, 5, 1]
print("Remove duplicates:", remove_duplicates_preserve_order(test_list))  # Output: [3, 5, 2, 1]


# Variation 1: Get list of duplicates from a list
"""
Note:
To find duplicates, track seen elements and add to duplicates list only when an element is encountered more than once.
"""

def get_duplicates(lst):
    seen = set()
    duplicates = []
    for item in lst:
        if item in seen and item not in duplicates:
            duplicates.append(item)
        else:
            seen.add(item)
    return duplicates

# Test case
print("Duplicates in list:", get_duplicates(test_list))  # Output: [3, 5]


# Variation 2: Remove duplicates from a number
"""
Note:
Convert number to string to treat digits as characters.
Use same logic as list to preserve order of digits without duplicates.
Return integer after joining unique digits.
"""

def remove_duplicates_from_number(num):
    digits = list(str(num))
    seen = set()
    result = []
    for d in digits:
        if d not in seen:
            seen.add(d)
            result.append(d)
    return int(''.join(result))

# Test case
test_num = 56789345678
print("Number after removing duplicates:", remove_duplicates_from_number(test_num))  # Output: 5678934


# Variation 3: Get list of duplicate digits from a number
def get_duplicates_from_number(num):
    digits = list(str(num))
    seen = set()
    duplicates = []
    for d in digits:
        if d in seen and d not in duplicates:
            duplicates.append(d)
        else:
            seen.add(d)
    return duplicates

# Test case
print("Duplicates in number:", get_duplicates_from_number(test_num))  # Output: ['5', '6', '7', '8']


# Variation 4: Remove duplicates from a string
def remove_duplicates_from_string(s):
    seen = set()
    result = []
    for ch in s:
        if ch not in seen:
            seen.add(ch)
            result.append(ch)
    return ''.join(result)

# Test case
test_str = "dfghjuytrertygcvhjert"
print("String after removing duplicates:", remove_duplicates_from_string(test_str))
# Output: "dfghjuytrevc"


# Variation 5: Get duplicates in a string
def get_duplicates_from_string(s):
    seen = set()
    duplicates = []
    for ch in s:
        if ch in seen and ch not in duplicates:
            duplicates.append(ch)
        else:
            seen.add(ch)
    return ''.join(duplicates)

# Test case
print("Duplicates in string:", get_duplicates_from_string(test_str))
# Output: "rgyhj"
