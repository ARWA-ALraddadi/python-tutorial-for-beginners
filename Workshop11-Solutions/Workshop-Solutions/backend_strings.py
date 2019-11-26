#--------------------------------------------------------------------#
#
# Staff Directory Back-End (character string version)
#
# A back-end function for returning employee details that match
# the given first/last-name prefix. The details are returned as
# lists containing (1) employee number, (2) first name, (3) last
# name and (4) date of birth. This version uses the
# Comma-Separated-Value text file as the data source, examining
# each line as a separate character string.
#

'''
These are some unit tests for the find_employees function.
Due to the artificial nature of the dataset, some prefixes
return a very large number of results and others return none.
Therefore, to keep these tests short, we have chosen to check
only the number of records returned or the first value
returned, rather than the full result set.

>>> len(find_employees('A'))
31946

>>> len(find_employees('Smee'))
181

>>> len(find_employees('Tis'))
173

>>> len(find_employees('Ze'))
1610

>>> len(find_employees('X'))
4868

>>> find_employees('Yish')[0]
['10043', 'Yishay', 'Tzvieli', '1960-09-19']

>>> find_employees('Bee')[0]
['10764', 'Yunming', 'Beetstra', '1953-01-12']

>>> find_employees('Shan')[0]
['10045', 'Moss', 'Shanbhogue', '1957-08-14']

>>> find_employees('Sho')[0]
['10398', 'Shooichi', 'Escriba', '1958-07-16']

>>> find_employees('Sm')[0]
['10533', 'Mohamadou', 'Smailagic', '1963-06-25']

>>> len(find_employees('Smith')) # A surprising result!
0

>>> len(find_employees('Jones')) # And another!
0
'''

def find_employees(prefix):
    # Initialise the list of employee details
    results = []
    # Open the text file for reading
    employees_file = open('employees.csv')
    # Examine each employee record
    for employee in employees_file:
        # Remove the newline
        fields = employee.replace('\n', '')
        # Extract the individual fields
        emp_no, birth_date, first_name, last_name, gender, hire_date = fields.split(',')
        # Save relevant details for employees whose names match the prefix
        if first_name.startswith(prefix) or last_name.startswith(prefix):
            results.append([str(emp_no), first_name, last_name, birth_date])
    # Close the text file
    employees_file.close()
    # Return the result
    return results

# A main program that executes the unit tests above only if this
# file is run directly rather than being imported into another module
if __name__ == "__main__":
    from doctest import testmod, REPORT_ONLY_FIRST_FAILURE
    print(testmod(verbose = False,
                  optionflags = REPORT_ONLY_FIRST_FAILURE))
