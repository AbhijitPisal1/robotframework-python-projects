# Question: Convert list of strings to integers (handle errors)
# Given a list of strings, convert each string to an integer if possible.
# If a string cannot be converted to an integer, handle the error gracefully (e.g., skip it).
# Example: ["10", "20", "abc", "30"] → [10, 20, 30]

"""
Approach:
Iterate over the input iterable.
For each element, attempt to convert it to an integer inside a try-except block.
If conversion succeeds, append the integer to the result list.
If conversion fails due to ValueError or TypeError, skip that element and continue.
This approach ensures robust conversion without crashing on invalid inputs.
"""

def convert_strings_to_ints(str_list):
    result = []
    for s in str_list:
        try:
            num = int(s)
            result.append(num)
        except (ValueError, TypeError):
            # Skip items that cannot be converted
            continue
    return result

"""
Note on variations:
- If the input list contains float strings or floats, convert each element to float first,
  then to int within the same try-except structure, e.g.:

      try:
          num = int(float(s))
          result.append(num)
      except (ValueError, TypeError):
          continue
"""
# Test cases:
test_str_list = ["10", "20", "abc", "30"]

print("Strings to ints:", convert_strings_to_ints(test_str_list))  # [10, 20, 30]

"""
To convert to float: use float(item)
To convert to string: use str(item)
To convert float-string to int: use int(float(item))
"""
