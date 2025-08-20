import array

# -------- Creating and Printing Arrays --------

print("Creating arrays:")
my_array = array.array('i')  # empty integer array
print("Empty array:", my_array)

my_array1 = array.array('i', [1, 2, 3, 4])
print("Initialized array:", my_array1)


# -------- Basic Insertions and Appending --------

print("\nBasic insertions and appending:")
arr1 = array.array('i', [1, 2, 3, 4])
print("Original array:", arr1)

arr1.insert(0, 6)  # insert at beginning
print("After inserting 6 at start:", arr1)
# Time Complexity: O(n)
# Insertion requires shifting elements after the position to the right.

arr1.insert(2, 7)  # insert in middle
print("After inserting 7 at index 2:", arr1)

arr1.insert(len(arr1), 8)  # insert at end
print("After inserting 8 at end:", arr1)
# Time Complexity: O(1) amortized
# Append is efficient unless the array needs to resize its underlying storage.

arr1.append(5)
print("After appending 5:", arr1)


# -------- Extending Arrays --------

print("\nExtending arrays:")

arr2 = array.array('i', [6, 7, 8, 9])
arr1.extend(arr2)
print("After extending with [6, 7, 8, 9]:", arr1)
# Time Complexity: O(k), where k is the length of the extended iterable
# More efficient than appending elements one by one in a loop.

list1 = [10, 11, 12]
arr1.fromlist(list1)
print("After adding from list [10, 11, 12]:", arr1)
# Time Complexity: O(k)
# Useful for efficiently adding multiple items from a Python list.

# -------- Traversing Arrays --------

print("\nTraversing array elements:")
for elem in arr1:
    print(elem, end=' ')
print()


# -------- Accessing Elements --------

def accessElement(arr, idx):
    if idx >= len(arr) or idx < -len(arr):
        print(f"Index {idx} out of bounds")
    else:
        print(f"Element at index {idx} is: {arr[idx]}")

accessElement(arr1, 0)    # first element
accessElement(arr1, -1)   # last element
accessElement(arr1, 100)  # out-of-bounds


# -------- Searching Elements --------

def linear_search(arr, target):
    for i, val in enumerate(arr):
        if val == target:
            return i
    return -1

print("\nSearching for 5 in array:", linear_search(arr1, 5))
print("Searching for 99 in array:", linear_search(arr1, 99))


# -------- Removing Elements --------

print("\nRemoving elements:")

arr1.remove(6)  # removes first occurrence of 6
print("After removing 6:", arr1)
# Time Complexity: O(n)
# Only removes the first matching value; raises ValueError if element not found.

popped = arr1.pop()
print(f"After popping last element ({popped}):", arr1)
# Time Complexity: O(1)
# Removes and returns the last element; raises IndexError if array is empty.y.


# -------- Additional Array Operations --------

print("\nAdditional operations:")

print("Index of element 8:", arr1.index(8))
# Time Complexity: O(n)
# Returns the index of the first occurrence; raises ValueError if not found.

arr1.reverse()
print("After reversing:", arr1)
# Time Complexity: O(n)
# Reverses the array in place; no new array is created.

print("Buffer info (address, length):", arr1.buffer_info())
# Returns a tuple with memory address and number of elements.

count_1 = arr1.count(1)
print("Count of element 1:", count_1)
# Time Complexity: O(n)
# Counts how many times a value appears in the array..

# Converting to bytes and back (note: tostring/fromstring deprecated)
byte_str = arr1.tobytes()
print(f"Byte string representation: {byte_str}")
new_arr = array.array('i')
new_arr.frombytes(byte_str)
print("Array reconstructed from bytes:", new_arr)
# Time Complexity: O(n)
# Used for serialization; note that tostring/fromstring are deprecated in Python 3.9+, prefer tobytes/frombytes.

print("Convert array to list:", arr1.tolist())
# Time Complexity: O(n)
# Converts the array into a Python list for flexible usage.

print("Slicing elements from index 1 to 4:", arr1[1:4])
# Time Complexity: O(k), where k is number of sliced elements
# Slicing creates a new array with the specified subset of elements.
