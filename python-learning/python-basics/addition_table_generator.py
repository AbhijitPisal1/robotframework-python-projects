
def addition_table(given_number):
    """
    This function generates an addition table for a given number, 
    printing a maximum of 5 lines or exiting if the result exceeds 20.
    It takes a parameter "given_number".
    """
    iterated_number = 1
    my_sum = 1  # Initialize "my_sum" to set its data type.
    """
    Loop until "iterated_number" exceeds 5.
    """
    while iterated_number <= 5:

        my_sum = given_number + iterated_number  # Calculate sum.

        if my_sum > 20:  # Exit if sum exceeds 20.
            break

        print(str(given_number), "+", str(iterated_number), "=", str(my_sum))  # Output the addition.

        iterated_number += 1  # Increment for the next iteration.


"""
Example calls:
"""
addition_table(5)
addition_table(17)
addition_table(30)

"""
Expected output:
5 + 1 = 6
5 + 2 = 7
5 + 3 = 8
5 + 4 = 9
5 + 5 = 10
17 + 1 = 18
17 + 2 = 19
17 + 3 = 20
None
"""