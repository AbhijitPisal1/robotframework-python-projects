"""
            ===================================
                    Python Decorators
            ===================================
"""
#==========================================
#         Simple Decorator        #
#==========================================
def simple_decorator(func):
    """
    A simple decorator that prints messages before and after the function runs.
    Demonstrates how decorators can add behavior to existing functions.
    """
    def wrapper():
        print("🌟 Before execution")
        func()
        print("✅ After execution")
    return wrapper

@simple_decorator
def greet():
    """Greets the Python learner. Demonstrates a function being decorated."""
    print("Hello, Python learner!")

print("\n=== Example 1: Simple Decorator ===")
print(greet.__doc__)
greet()

#============================================
#     Decorator with Function Arguments    #
#============================================
def log_arguments(func):
    """
    A decorator that logs the function call with its arguments and result.
    Demonstrates handling functions with arbitrary arguments (*args, **kwargs).
    """
    def wrapper(*args, **kwargs):
        print(f"📘 Calling {func.__name__} with {args} {kwargs}")
        result = func(*args, **kwargs)
        print(f"📗 {func.__name__} returned {result}")
        return result
    return wrapper

@log_arguments
def add(a, b):
    """Adds two numbers and demonstrates logging decorator."""
    return a + b

print("\n=== Example 2: Decorator with Arguments ===")
print(add.__doc__)
add(3, 5)

#==========================================
#     Decorator with Parameters    #
#==========================================
def repeat(n):
    """
    A decorator factory that repeats the execution of a function n times.
    Demonstrates how to pass arguments to a decorator itself.
    """
    def decorator(func):
        def wrapper(*args, **kwargs):
            for i in range(n):
                print(f"🔁 Run {i+1} of {n}")
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)
def cheer():
    """Prints an encouraging message, repeated by repeat decorator."""
    print("Python is awesome!")

print("\n=== Example 3: Decorator with Parameters ===")
print(cheer.__doc__)
cheer()

#==========================================
#         Multiple Decorators        #
#==========================================
def uppercase(func):
    """Converts the return value of the function to uppercase."""
    def wrapper():
        return func().upper()
    return wrapper

def exclaim(func):
    """Adds an exclamation mark to the return value of the function."""
    def wrapper():
        return func() + "!"
    return wrapper

@uppercase
@exclaim
def greet_text():
    """Returns a greeting string decorated by multiple decorators."""
    return "hello"

print("\n=== Example 4: Multiple Decorators ===")
print(greet_text.__doc__)
print(greet_text())

#==========================================
#         Built-in Decorator Example        #
#==========================================
from functools import lru_cache

@lru_cache(maxsize=5)
def fib(n):
    """
    Computes Fibonacci numbers using caching to optimize repeated calls.
    Demonstrates use of Python's built-in @lru_cache decorator.
    """
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)

print("\n=== Example 5: Built-in Decora tor (Fibonacci caching) ===")
print(fib.__doc__)
print(f"fib(10) = {fib(10)}")

print("\n✅ End of demonstration.")


"""
SUMMARY
-----------------
--> A decorator wraps a function and can modify or extend its behavior.  
--> Syntax: `@decorator_name` above a function definition.  
--> They help keep your code DRY (Don’t Repeat Yourself).  
--> You can pass arguments to both the function and the decorator.  
--> Common for logging, validation, caching, timing, etc.
"""