# This block of code updates the year in a list of dates.
# The existing "years" list is provided. 
years = ["January 2023", "May 2025", "April 2023", "August 2024", "September 2025", "December 2023"]

# Initializes "updated_years" as an empty list to store the updated years.
updated_years = []

# Iterates through each "year" in the "years" list.
for year in years:

    # Checks if the "year" ends with "2023".
    if year.endswith("2023"):

        # Replaces "2023" with "2024" in a temporary variable "new".
        new = year.replace("2023", "2024")

        # Appends the modified element to "updated_years".
        updated_years.append(new)

    # If it doesn't end with "2023", appends the original "year" unchanged.
    else:
        updated_years.append(year)

print(updated_years)
# Expected output: ["January 2024", "May 2025", "April 2024", "August 2024", "September 2025", "December 2024"]

# This block of code updates the year using a different approach via list comprehension.
# The existing "years" list is provided.
years = ["January 2023", "May 2025", "April 2023", "August 2024", "September 2025", "December 2023"]

# List comprehension generates a new list "updated_years" that replaces "2023" 
# with "2024" if the last four characters of "year" are "2023"; otherwise, it 
# retains the original "year".
updated_years = [year.replace("2023", "2024") if year[-4:] == "2023" else year for year in years]

print(updated_years)
# Expected output: ["January 2024", "May 2025", "April 2024", "August 2024", "September 2025", "December 2024"]

'''
Created on Jul 18, 2023

@author: APisal
'''