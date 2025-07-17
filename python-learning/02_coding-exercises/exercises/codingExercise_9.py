"""
Customized Greeting Based on Time of Day
Create a variable hour and assign the value 16.

Use if-elif-else statements to print:

"Good Morning" if the hour is between 5 and 11,
"Good Afternoon" if the hour is between 12 and 17,
"Good Evening" if the hour is between 18 and 21,
"Good Night" for all other hours.

Print "Greeting code has completed."

Expected Output:
For input 10:
Good Morning
Greeting code has completed.

For input 15:
Good Afternoon
Greeting code has completed.
"""

hour = 16  # Change this to test different times

if 5 <= hour <= 11:
    print("Good Morning")
elif 12 <= hour <= 17:
    print("Good Afternoon")
elif 18 <= hour <= 21:
    print("Good Evening")
else:
    print("Good Night")

print("Greeting code has completed.")
