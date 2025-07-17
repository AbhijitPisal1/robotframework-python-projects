# Counts from start to stop, either counting up or down.
def counter(start, stop):
    if start > stop:
        return_string = "Counting down: "
        while start >= stop:
            return_string += str(start)  # Append the current number to the return string
            if start > stop:
                return_string += ","  # Add a comma if not at the last number
            start -= 1  # Decrement the start variable for counting down
    else:
        return_string = "Counting up: "
        while stop >= start:
            return_string += str(start)  # Append the current number to the return string
            if start < stop:
                return_string += ","  # Add a comma if not at the last number
            start += 1  # Increment the start variable for counting up
    return return_string  # Return the complete counting string

print(counter(1, 10)) # Should output "Counting up: 1,2,3,4,5,6,7,8,9,10"
print(counter(2, 1)) # Should output "Counting down: 2,1"
print(counter(5, 5)) # Should output "Counting up: 5"

'''
Created on Jul 18, 2023

@author: APisal
'''