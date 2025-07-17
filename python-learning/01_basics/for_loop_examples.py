# The for loop is an iterative control structure used to execute a block of code repeatedly over a sequence (such as a list, tuple, string, or range).
# The loop variable takes on the value of each element in the sequence, one by one, from start to end.
# The block of code inside the for loop is executed once for each element in the sequence.
# The loop automatically stops when all items in the sequence have been processed.
# The for loop is commonly used for counting, iterating over items, or performing repeated operations on elements in a collection.

######################## DEMO 1 ##############################
# This demo iterates through a list of integers using a for loop.
# This demonstrates how a for loop can be used with lists and how conditional logic (if-else) can be used inside the loop.
obj1 = [2, 3, 4, 5, 6, 7]

for element in obj1:
    if element % 2 == 0:
        print("{} {}".format(element, " is even number"))
    else:
        print("{} {}".format(element, " is odd number"))
print("for loop demo completed")
######################## DEMO 2 ##############################
# The range function is used with parameters (1, 6), which includes numbers from 1 to 5.
# This demonstrates how to use a for loop with a numeric range to accumulate values.

sum1 = 0
for i in range(1,6):    # range (i,j) -> i to j-1   with default increment of 1
    print(i)
    sum1 = sum1+i
print("{} {}".format("sum of numbers is", sum1))
######################## DEMO 3 ##############################
# This demo calculates the sum of the first five odd natural numbers starting from 1:
# This demonstrates how to control the step/increment in a for loop.

sum2 = 0
for k in range(1, 10 , 2):    # range (i,j) -> i to j-1
    print(k)
    sum2 = sum2+k
print("{} {}".format("sum of numbers is", sum2))
