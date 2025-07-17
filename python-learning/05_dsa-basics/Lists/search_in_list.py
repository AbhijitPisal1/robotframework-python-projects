# ----------------------------------------
# Searching for an Element in the List
# ----------------------------------------

my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90]

# Using 'in' operator --> Time Complexity: O(n)
target = 50
if target in my_list:
    print(f"{target} is in the list")
else:
    print(f"{target} is not in the list")

# Linear Search Implementation
def linearSearch(p_list, p_target):
    for i, value in enumerate(p_list):
        if value == p_target:
            return i
    return 'target item does not exist'

print(linearSearch(my_list, 20))

"""
Note:
- enumerate() is used to access both index and value during iteration.
- Equivalent version without enumerate:

def linearSearch(p_list, p_target):
    for i in range(len(p_list)):
        if p_list[i] == p_target:
            return i
    return 'target item does not exist'
"""

# ----------------------------------------
# Calculating Average Using List
# ----------------------------------------

my_list1 = []
while True:
    inp = input("Enter a number: ")
    if inp == 'done':
        break
    value = float(inp)
    my_list1.append(value)

if len(my_list1) > 0:
    average = sum(my_list1) / len(my_list1)
    print('Average:', average)
else:
    print('No numbers were entered.')

"""
Instead of using:
    total = total + value
    count = count + 1
We use a list to store values, then:
    - sum() gives total
    - len() gives count

Advantages:
- Cleaner code
- More flexible (e.g., easy to sort, find median, etc.)

manual variable management approach 
total = 0
count = 0

while True:
    inp = input("Enter a number: ")
    if inp == 'done':
        break
    value = float(inp)      # Convert input directly to float
    total = total + value   # Add value to total
    count = count + 1       # Increase count by 1

average = total / count
print('Average:', average)
"""