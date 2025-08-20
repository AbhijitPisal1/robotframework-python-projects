# Example list for demonstrating different time complexities
numbers = [1, 2, 3, 4, 5]

print("### Constant Time Complexity (O(1)) ###")
# Accessing a single element takes constant time
print(numbers[0])

print("\n### Linear Time Complexity (O(n)) ###")
# Iterating through all elements once is linear time
for num in numbers:
    print(num)

print("\n### Logarithmic Time Complexity (O(log n)) - simulated by stepping")
# Simulate logarithmic by jumping steps (not a perfect example but illustrates skipping)
for idx in range(0, len(numbers), 2):
    print(numbers[idx])

print("\n### Quadratic Time Complexity (O(n^2)) ###")
# Nested loops cause quadratic growth in operations
for x in numbers:
    for y in numbers:
        print(x, y)

print("\n### Exponential Time Complexity (O(2^n)) - Fibonacci Example ###")

def fibonacci(num):
    if num <= 1:
        return num
    return fibonacci(num - 1) + fibonacci(num - 2)

print(fibonacci(5))  # Smaller input to avoid long delays

print("\n### Combining operations: Addition vs Multiplication of arrays ###")

listA = [1, 2, 3, 4, 5, 6, 7, 8, 9]
listB = [11, 12, 13, 14, 15, 16, 17, 18, 19]

print("Iterate over listA:")
for a in listA:
    print(a)

print("Iterate over listB:")
for b in listB:
    print(b)

print("Nested iteration over listA and listB:")
for a in listA:
    for b in listB:
        print(a, b)

print("\n### Iterative approach: Finding max value in a list ###")

sample_data = [1, 10, 45, 33, 23, 45, 67, 2, 3, 33, 55, 11, 65, 76, 34, 35, 27, 99]

def find_max_iterative(arr):
    max_val = arr[0]  # constant time operation
    for i in range(1, len(arr)):  # linear time loop
        if arr[i] > max_val:      # constant time comparison
            max_val = arr[i]      # constant time assignment
    print(max_val)  # constant time output

find_max_iterative(sample_data)

print("\n### Recursive approach: Finding max value in a list ###")

def find_max_recursive(arr, n):
    if n == 1:
        return arr[0]
    return max(arr[n - 1], find_max_recursive(arr, n - 1))

print(find_max_recursive(sample_data, len(sample_data)))

print("\n### Recursive calls with multiple calls example ###")

def double_recursive(n):
    if n <= 1:
        return 1
    return double_recursive(n - 1) + double_recursive(n - 1)

print(double_recursive(3))
