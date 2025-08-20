"""
1. count_by_tens(end): Returns numbers from 0 to end stepping by 10 as a space-separated string.
2. count_digits(n): Counts digits in an integer including zero.
3. multiples_of_10_upto_100(): Lists multiples of 10 between 1 and 100.
4. count_integer_factors(n): Counts integer factors of n; returns 0 if n is zero.
5. get_nth_word(sentence, n): Returns the nth word of a sentence or None if invalid.
6. print_multiplication_table(start, stop): Prints multiplication table from start to stop.
7. odd_numbers_list(n): Returns a list of odd numbers from 1 to n.
8. is_power_of_base(number, base): Checks if number is a power of base recursively.
9. round_to_nearest_10(number): Rounds number to nearest multiple of 10.
10. list_of_squares(start, end): Returns list of squares from start to end.
11. recursive_sum_to_n(n): Recursively sums all integers from 1 to n.
12. convert_seconds_to_hms(seconds): Converts seconds to (hours, minutes, seconds).
13. squares(start, end): Generates list of squares between start and end.
14. odd_numbers(n): Returns odd numbers from 1 to n inclusive.
"""

# 1. Count by 10
def count_by_tens(end):
    """
    Uses a list comprehension to generate numbers from 0 up to 'end' (inclusive) stepping by 10.
    Converts each number to a string, then joins them with spaces into one string.
    """
    return ' '.join([str(num) for num in range(0, end + 1, 10)])

print("1. count_by_tens(100):")
print(count_by_tens(100))
print()

# 2. Count number of digits
def count_digits(n):
    """
    Handles zero as a special case directly returning 1.
    For other numbers, takes the absolute value to ignore sign,
    converts it to string and uses the string length to count digits.
    """
    return 1 if n == 0 else len(str(abs(n)))

print("2. count_digits examples:")
print(count_digits(25))     # 2
print(count_digits(144))    # 3
print(count_digits(1000))   # 4
print(count_digits(0))      # 1
print()

# 3. Multiples of 10 using list comprehension
def multiples_of_10_upto_100():
    """
    Iterates over numbers from 1 to 100,
    selecting only those divisible evenly by 10 using modulo operation,
    collecting them into a list via list comprehension.
    """
    return [x for x in range(1, 101) if x % 10 == 0]

print("3. multiples_of_10_upto_100():")
print(multiples_of_10_upto_100())
print()

# 4. Count integer factors
def count_integer_factors(n):
    """
    Returns 0 immediately if input is zero to avoid infinite factors.
    Otherwise, uses a list comprehension to check every number from 1 to n,
    testing divisibility (no remainder),
    then counts the length of this list to get total factors.
    """
    if n == 0:
        return 0
    return len([i for i in range(1, n+1) if n % i == 0])

print("4. count_integer_factors examples:")
print(count_integer_factors(0))    # 0
print(count_integer_factors(3))    # 2
print(count_integer_factors(10))   # 4
print(count_integer_factors(24))   # 8
print()

# 5. Get nth word from a sentence
def get_nth_word(sentence, n):
    """
    Splits the sentence into words by whitespace.
    Checks if n is positive and within bounds.
    Returns the (n-1)th index word to match 1-based indexing.
    Returns None if n is invalid or out of range.
    """
    if n > 0:
        words = sentence.split()
        if n <= len(words):
            return words[n - 1]

print("5. get_nth_word examples:")
print(get_nth_word("This is a lesson about lists", 4))  # lesson
print(get_nth_word("This is a lesson about lists", -4)) # None
print(get_nth_word("Now we are cooking!", 5))           # None
print()

# 6. Multiplication table printer
def print_multiplication_table(start, stop):
    """
    Uses nested loops from start to stop inclusive.
    Outer loop iterates over rows (x), inner loop over columns (y).
    Prints the product of x and y followed by space without newline.
    After inner loop finishes, prints newline to start next row.
    """
    for x in range(start, stop + 1):
        for y in range(start, stop + 1):
            print(str(x * y), end=" ")
        print()

print("6. print_multiplication_table(1, 5):")
print_multiplication_table(1, 5)
print()

# 7. List of odd numbers using list comprehension
def odd_numbers_list(n):
    """
    Iterates from 1 to n inclusive,
    checks oddness using modulo 2,
    collects odd numbers into a list,
    returns empty list if n is less than 1.
    """
    return [x for x in range(1, n + 1) if x % 2 == 1]

print("7. odd_numbers_list examples:")
print(odd_numbers_list(5))    # [1, 3, 5]
print(odd_numbers_list(10))   # [1, 3, 5, 7, 9]
print(odd_numbers_list(11))   # [1, 3, 5, 7, 9, 11]
print(odd_numbers_list(1))    # [1]
print(odd_numbers_list(-1))   # []
print()

# 8. Check if number is power of base (recursive)
def is_power_of_base(number, base):
    """
    Recursively divides number by base if number is at least base.
    If number becomes less than base, checks if it's exactly 1.
    Returns True if number reduces perfectly down to 1 by division steps,
    False otherwise.
    """
    if number < base:
        return number == 1
    return is_power_of_base(number / base, base)

print("8. is_power_of_base examples:")
print(is_power_of_base(8, 2))     # True
print(is_power_of_base(64, 4))    # True
print(is_power_of_base(70, 10))   # False
print()

# 9. Round up to nearest multiple of 10
def round_to_nearest_10(number):
    """
    Adds 5 to the input number to handle rounding up.
    Uses integer division by 10 to truncate digits after rounding.
    Multiplies back by 10 to get the nearest multiple of 10.
    """
    return ((number + 5) // 10) * 10

print("9. round_to_nearest_10(35):")
print(round_to_nearest_10(35))    # 40
print()

# 10. List of squares using list comprehension
def list_of_squares(start, end):
    """
    Iterates through the range from start to end inclusive.
    Squares each number by multiplying it by itself.
    Collects all squares in a list using list comprehension.
    """
    return [n * n for n in range(start, end + 1)]

print("10. list_of_squares examples:")
print(list_of_squares(2, 3))      # [4, 9]
print(list_of_squares(1, 5))      # [1, 4, 9, 16, 25]
print(list_of_squares(0, 10))     # [0, 1, 4, ..., 100]
print()

# 11. Recursive sum of positive numbers
def recursive_sum_to_n(n):
    """
    Defines base case: sum up to 1 or 0 returns n itself.
    Recursively calls itself with n-1 and adds current n to result.
    Builds up sum by stacking recursive calls until base case reached.
    """
    if n <= 1:
        return n
    return n + recursive_sum_to_n(n - 1)

print("11. recursive_sum_to_n examples:")
print(recursive_sum_to_n(3))      # 6
print(recursive_sum_to_n(5))      # 15
print()

# 12. Convert seconds to hours, minutes, seconds
def convert_seconds_to_hms(seconds):
    """
    Calculates hours by integer division of seconds by 3600.
    Minutes are computed by removing hours (mod 3600),
    then integer dividing by 60.
    Remaining seconds are what's left after extracting hours and minutes.
    Returns three components as a tuple.
    """
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    remaining_seconds = seconds % 60
    return hours, minutes, remaining_seconds

print("12. convert_seconds_to_hms(5000):")
h, m, s = convert_seconds_to_hms(5000)
print(f"{h} hours, {m} minutes, {s} seconds")
print()

# 13. Squares list generator
def squares(start, end):
    """
    This list comprehension generates a list of squared numbers (n*n)
    and takes two integer parameters.

    The list comprehension computes the square of an integer "n,"
    which ranges from "start" to "end" inclusively.
    To include the endpoint in range(), add +1 to the end value.
    """
    return [n * n for n in range(start, end + 1)]

print("13. squares examples:")
print(squares(2, 3))              # [4, 9]
print(squares(1, 5))              # [1, 4, 9, 16, 25]
print(squares(0, 10))             # [0, 1, 4, ..., 100]
print()

# 14. List of odd numbers
def odd_numbers(n):
    """
    The odd_numbers function returns a list of odd numbers between 1 and n,
    inclusively.

    It uses a list comprehension to iterate over the range from 1 to n inclusive,
    filtering numbers with remainder 1 when divided by 2 (odd numbers).
    Returns an empty list if n is less than 1.
    """
    return [x for x in range(1, n + 1) if x % 2 == 1]

print("14. odd_numbers examples:")
print(odd_numbers(5))             # [1, 3, 5]
print(odd_numbers(10))            # [1, 3, 5, 7, 9]
print(odd_numbers(11))            # [1, 3, 5, 7, 9, 11]
print(odd_numbers(1))             # [1]
print(odd_numbers(-1))            # []