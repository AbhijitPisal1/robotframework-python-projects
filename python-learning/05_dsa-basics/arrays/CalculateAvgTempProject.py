# Project Statement:
# Create a Python program that accepts daily high temperatures for a given number of days,
# calculates the average temperature, and reports how many days had temperatures above the average using a list.

# Input number of days
num_days = int(input("How many days' temperature? : "))

temperatures = []

# Collect temperatures
for i in range(num_days):
    temp = int(input(f"Day {i + 1}'s High Temperature: "))
    temperatures.append(temp)

# Calculate average
avg_temp = round(sum(temperatures) / num_days, 2)
print(f"\nAverage Temperature over {num_days} day(s) is: {avg_temp}")

# Find and count days above average
above_avg_days = 0
for i, temp in enumerate(temperatures):
    if temp > avg_temp:
        above_avg_days += 1
        print(f"Temperature of Day {i + 1} ({temp}) is above average.")

print(f"\nTotal {above_avg_days} day(s) are above average.")
