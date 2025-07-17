# This function checks a schedule entry for an old date and replaces it with a new date if found.
def replace_date(schedule, old_date, new_date):
    # Verifies if "old_date" is at the end of the "schedule" string.
    if schedule.endswith(old_date):
        # If true, holds the length of "old_date".
        p = len(old_date)

        # Constructs "new_schedule" by removing "old_date" and inserting "new_date".
        new_schedule = schedule[:-p] + schedule[-p:].replace(old_date, new_date)

        # Returns the updated schedule.
        return new_schedule

    # If "old_date" is not found at the end, returns the original schedule unmodified.
    return schedule


print(replace_date("Last year’s annual report will be released in March 2023", "2023", "2024"))
# Should display "Last year’s annual report will be released in March 2024"
print(replace_date("In April, the CEO will hold a conference", "April", "May"))
# Should display "In April, the CEO will hold a conference"
print(replace_date("The convention is scheduled for October", "October", "June"))
# Should display "The convention is scheduled for June"


'''
Created on Jul 18, 2023

@author: APisal
'''