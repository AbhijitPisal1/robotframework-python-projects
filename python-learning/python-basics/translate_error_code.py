"""This function accepts a variable "error_code" as a parameter."""
def translate_error_code(error_code):
    """The if-elif-else block evaluates the value of "error_code".
    The if statement uses the equality operator == for comparison."""
    if error_code == "401 Unauthorized":
        """Assigns a translation if the error code matches."""
        translation = "Server received an unauthenticated request"

    elif error_code == "404 Not Found":
        """Assigns a translation if the error code matches."""
        translation = "Requested web page not found on server"

    elif error_code == "408 Request Timeout":
        """Assigns a translation if the error code matches."""
        translation = "Server request to close unused connection"

    else:
        """If none of the conditions are met, assign a default translation."""
        translation = "Unknown error code"

    """Return the translation from the if-elif-else block."""
    return translation


"""Display the output by calling the function with an error code."""
print(translate_error_code("404 Not Found"))

# Expected output:
# Requested web page not found on server