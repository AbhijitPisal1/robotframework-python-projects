# The if-else block is a conditional control structure used to execute different blocks of code based on whether a condition is True or False.
# The if statement evaluates a condition. If the condition is True, the indented block under if is executed.
# The else block is optional and runs if the condition in the if statement is False.
# The conditions used in if, elif, or else must result in a Boolean value (True or False).

######################## DEMO 1 ##############################
# This demo shows a simple if-else conditional check.
# It compares a string variable 'greeting' with a target string "Morning".
# In Python, ':' acts as an opening brace, and indentation defines the code block.
# If the condition is True, it executes the if-block; otherwise, it goes to the else-block.

greeting = "Good Morning"

if greeting == "Morning":
    print("Condition matches")
else:
    print("condition does not matches")
print("if else condition code is completed")

######################## DEMO 1 ##############################
# This demo evaluates a student's marks and assigns a grade based on specific ranges.
# It uses a chained if-elif-else structure to check which range the marks fall into.
# Logical operators (and, >, <=) are used to define ranges.
# Only the first matching condition executes — the rest are skipped once a match is found.

marks = 75

if marks <= 100 and marks > 90:
    print("A Grade")
elif marks <= 90 and marks > 75:
    print("B Grade")
elif marks <= 75 and marks > 60:
    print("C Grade")
elif 60 >= marks > 45:      # simplifying chained reaction
    print("D Grade")
elif marks <= 45:
    print("e Grade")
print("Evaluation done")