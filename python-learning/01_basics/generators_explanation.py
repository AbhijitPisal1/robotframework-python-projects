"""
        ==================================
                Python Generators
        ==================================
"""
#==========================================
#     count_up_to() Generator    #
#==========================================
def count_up_to(n):
    """
    Generator that yields numbers from 1 up to n, one at a time.
    Demonstrates how yield produces values lazily, saving memory.
    """
    i = 1
    while i <= n:
        yield i
        i += 1

print("\n=== Example 1: count_up_to() Generator ===")
print(count_up_to.__doc__)
for num in count_up_to(5):
    print(num, end=" ")
print("\n")

#==========================================
#     Normal function vs Generator    #
#==========================================
def normal_list(n):
    """Returns a full list from 0 to n-1"""
    return [i for i in range(n)]

def generator_list(n):
    """Yields numbers from 0 to n-1 lazily"""
    for i in range(n):
        yield i

print("\n=== Example 2: Normal function vs Generator ===")
print(normal_list(5))  # Normal list
for val in generator_list(5):
    print(val, end=" ")  # Generator
print("\n")

#==============================================
#        Fibonacci Infinite Generator        #
#==============================================
def fibonacci():
    """
    Infinite Fibonacci sequence generator.
    Each next() call produces the next number without storing all previous numbers.
    """
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

print("\n=== Example 3: Fibonacci Infinite Generator ===")
print(fibonacci.__doc__)
fib = fibonacci()
for _ in range(6):
    print(next(fib), end=" ")
print("\n")

#==========================================
#        Chaining Generators        #
#==========================================
def numbers():
    """Yields numbers from 1 to 5"""
    for i in range(1, 6):
        yield i

def squares(nums):
    """Yields square of each number from an input generator"""
    for n in nums:
        yield n * n

def even(nums):
    """Yields only even numbers from an input generator"""
    for n in nums:
        if n % 2 == 0:
            yield n

print("\n=== Example 4: Chaining Generators (numbers → squares → even) ===")
result = even(squares(numbers()))
for val in result:
    print(val, end=" ")
print("\n")

#==========================================
#        Generator Expression        #
#==========================================
print("\n=== Example 5: Generator Expression ===")
squares_expr = (x*x for x in range(5))
for val in squares_expr:
    print(val, end=" ")
print("\n")

print("\n✅ End of demonstration.")
