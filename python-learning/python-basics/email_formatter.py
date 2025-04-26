# Generates a list of formatted email strings from a list of tuples
# containing names and corresponding email addresses.
def full_emails(people):
    result = []
    for email, name in people:
        result.append("{}<{}>".format(name, email))  # Format each name and email and add to the result list
    return result  # Return the list of formatted strings

print(full_emails([("Alex morgan", "alexM@gmail.com"), ("john williams", "Johnwill@test.com")]))

'''
Created on Jul 18, 2023

@author: APisal
'''