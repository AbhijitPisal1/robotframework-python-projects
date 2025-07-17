######################## FUNCTION DEMO ##############################
# A function is a group of related statements that performs a specific task.
# This function greets a user by name.

# Function Declaration:
# def - keyword used to define a function
# GreetUser - name of the function (identifier)
# username - parameter that the function accepts (input)

def GreetUser(username):
    print("Hello, " + username + "! Welcome to the Python course.")

# Function call with your name
GreetUser("John")

######################## FUNCTION DEMO 2 ##############################

# This function adds two integers and prints the result.
# It does NOT return the result to the caller, so it cannot be reused or stored.
def addIntegers(a, b):
    print(a+b)

addIntegers(2, 3)

######################## FUNCTION DEMO 3 ##############################

# This function multiplies two integers and returns the result.
# Because it uses 'return', the result can be stored, reused, or printed later
def multiplyIntegers(a, b):
    return  a*b


print(multiplyIntegers(3,4))