import numpy as np

# -------- Creating 2D arrays --------

# Creating a 2D NumPy array (3 rows × 4 columns)
twoDarray = np.array([[1, 3, 5, 7], [2, 4, 6, 8], [10, 20, 30, 40]])
print("Original 2D array:\n", twoDarray)

# Creating another 2D NumPy array (3 rows × 5 columns)
arr1 = np.array([[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]])
print("\nAnother 2D array:\n", arr1)

# Time & Space Complexity:
# O(n * m) where n = number of rows, m = number of columns

# -------- Inserting rows and columns --------

print("\nAdding a new column at the start:")
arr2 = np.insert(twoDarray, 0, np.array([[0, 1, 2]]), axis=1)
print(arr2)
# axis=1 inserts column; inserted values length must match number of rows

print("\nAdding a new row at the start:")
arr3 = np.insert(twoDarray, 0, np.array([[100, 200, 300, 400]]), axis=0)
print(arr3)
# axis=0 inserts row; inserted values length must match number of columns

print("\nAdding a new row at the second position:")
arr4 = np.insert(twoDarray, 1, np.array([[50, 150, 250, 350]]), axis=0)
print(arr4)

print("\nAdding a new row at the end:")
arr5 = np.append(twoDarray, np.array([[100, 200, 300, 400]]), axis=0)
print(arr5)
# np.append with axis=0 adds row at the bottom

# -------- Accessing elements --------

def accessElements(array, rowIndex, colIndex):
    if rowIndex >= len(array) or colIndex >= len(array[0]):
        print("incorrect Index")
    else:
        print(f"Element at ({rowIndex}, {colIndex}):", array[rowIndex][colIndex])

# Access time complexity: O(1)
# Space complexity: O(1)

accessElements(arr1, 2, 3)  # valid access example

# -------- Traversing 2D array --------

def traverseInArray(array):
    print("\nTraversing 2D array elements:")
    for i in range(len(array)):
        for j in range(len(array[0])):
            print(array[i][j], end=' ')
        print()

# Traversing time complexity: O(n*m)
# Space complexity: O(1)

traverseInArray(arr1)

# -------- Searching in 2D array --------

def searchInArray(array, value):
    for i in range(len(array)):
        for j in range(len(array[0])):
            if array[i][j] == value:
                return f"The value is located at index ({i}, {j})"
    return "The element is not found"

print("\nSearch results:")
print(searchInArray(arr1, 14))
print(searchInArray(arr1, 99))

# Searching time complexity: O(n*m)
# Space complexity: O(1)

# -------- Deleting rows and columns --------

print("\nDeleting first column from arr1:")
arr2 = np.delete(arr1, 0, axis=1)  # Delete first column
print(arr2)

print("\nDeleting third row from arr1:")
arr3 = np.delete(arr1, 2, axis=0)  # Delete third row
print(arr3)

# Deletion time complexity: O(n*m) due to data copying
# Space complexity: O(n*m) since a new array is created
