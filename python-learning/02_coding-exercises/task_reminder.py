# A function is defined using the def() keyword, with "time_as_string"
# as its parameter that will be provided upon the function call.
def task_reminder(time_as_string):

    # This if-elif-else block assigns a string to "task" based on specific 
    # conditions, using the == operator for equality comparisons. For 
    # example, if the parameter is "11:30 a.m.", then "task" will be 
    # "Run TPS report".
    if time_as_string == "8:00 a.m.":
        task = "Check overnight backup images"
    elif time_as_string == "11:30 a.m.":
        task = "Run TPS report"
    elif time_as_string == "5:30 p.m.":
        task = "Reboot servers"
    # The else statement handles all other values of "time_as_string" 
    # not covered in the if-elif block.
    else:
        task = "Provide IT Support to employees"

    # This line returns the value of "task" back to the function call.
    return task

# This line calls the function with "10:00 a.m." as the argument.
print(task_reminder("10:00 a.m."))
# Expected output: "Provide IT Support to employees"


'''
Created on Jul 17, 2023

@author: APisal
'''