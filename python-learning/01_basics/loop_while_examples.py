######################## DEMO 1 ##############################
# This is a basic while loop that counts down from 4 to 2
# There is no fixed number of iterations; it depends on the value and update of num1.
# This demonstrates the general behavior of a while loop:
#   - As long as the condition is True, the loop continues.
#   - If the condition is never made False, it could result in an infinite loop.

num1 = 4

while num1 > 1:
    print(num1)
    num1 = num1 -1

print("while loop execution is done")

######################## DEMO 2 ##############################
# This demo shows how you can use conditions (if-else) inside loops to make decisions for each iteration.
# The modulo operator (%) is used to determine odd/even:
#   - If num2 % 2 != 0 → odd
#   - Else → even

num2 = 10

while num2 > 1:
    if num2 % 2 != 0:
      print("{}{}".format(num2," is odd number"))
    else:
        print("{}{}".format(num2," is even number"))
    num2 = num2 -1
print("While loop execution is done")

######################## DEMO 3 ##############################
# The break statement immediately ends the nearest enclosing loop (for or while), even if the loop condition is still True.
# It is often used to:
    # Exit a loop early when a condition is met.
    # Avoid unnecessary iterations.
    # Handle search or escape scenarios (like breaking out when an item is found).
num3 = 6

while num3 > 1:
    if num3 == 3:
        break
    print(num3)
    num3 = num3-1
print("Break statement while loop demo is done")

######################## DEMO 4 ##############################
# The continue statement skips the current iteration of the loop and goes directly to the next iteration.
# It’s often used to:
    # Ignore specific values
    # Skip processing certain conditions
    # Keep the loop going but avoid executing some part of its body under specific cases
num4 = 8
while num4 > 1:
    if num4 ==7:
        num4 = num4 -1
        continue
    if num4 == 3:
        print("3 found. break now")
        break
    print(num4)
    num4 = num4 -1