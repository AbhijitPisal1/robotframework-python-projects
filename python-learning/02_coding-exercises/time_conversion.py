# Question: Converts a total number of seconds into hours, minutes, and remaining seconds.
def convert_seconds(seconds):
    hours = seconds // 3600  # Calculate hours by dividing total seconds by 3600
    minutes = (seconds - hours * 3600) // 60  # Calculate remaining minutes
    remaining_seconds = seconds - hours * 3600 - minutes * 60  # Calculate remaining seconds
    return hours, minutes, remaining_seconds  # Return hours, minutes, and remaining seconds


hour, minute, second = convert_seconds(5000)
print(hour, minute, second)

'''
Created on Jul 17, 2023

@author: APisal
'''