def intersection(list1, list2):
    """Find the intersection of two lists."""
    return list(set(list1) & set(list2))  # Use set intersection


# Example usage:
list_a = [1, 2, 3, 4, 5]
list_b = [4, 5, 6, 7, 8]
result = intersection(list_a, list_b)
print(f"Intersection of {list_a} and {list_b}: {result}")  # Output: [4, 5]

""" alternatively, Find the intersection of two lists using list comprehension.
def intersection(list1, list2):
    return [value for value in list1 if value in list2]

# Example usage:
list_a = [1, 2, 3, 4, 5]
list_b = [4, 5, 6, 7, 8]
result = intersection(list_a, list_b)
print(f"Intersection of {list_a} and {list_b}: {result}")  # Output: [4, 5]"""
