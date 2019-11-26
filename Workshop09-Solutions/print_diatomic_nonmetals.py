#---------------------------------------------------------
#
# Print diatomic nonmetals
#
# In this exercise you will develop a Python program that
# accesses an SQLite database.  We assume that you have
# already loaded a version of the Elements database using
# the a graphical user interface.  You can do so by importing
# the elements.sql script provided.
#
# Your tasks:
#
# 1) Browse the database's contents in an interactive interface
# to ensure that you're familiar with its two tables and
# their columns.
#
# 2) Write a Python program to print both the names and symbols
# of the "diatomic nonmetals" in our small database.  These
# are the elements with atomic numbers 1, 7-9 and 17.
#



#---------------------------------------------------------

# Import the SQLite functions
from sqlite3 import *

## DEVELOP YOUR PROGRAM HERE BY REPLACING EACH OF THE 'pass'
## STATEMENTS BELOW (WHICH DO NOTHING) WITH THE NECESSARY CODE

# 1. Make a connection to the elements database
connection = connect(database = "elements.db")

# 2. Get a cursor on the database
elements = connection.cursor()

# 3. Construct the SQLite query
query = '''SELECT atomic_numbers.element_name, symbol, atomic_number
           FROM atomic_numbers, symbols
           WHERE atomic_number IN (1, 7, 8, 9, 17)
           AND atomic_numbers.element_name = symbols.element_name
           ORDER BY atomic_number'''

# 4. Execute the query
elements.execute(query)

# 5. Get the result set and print it out
rows = elements.fetchall()
for row in rows:
    name, symbol, number = row
    print(name + ' (' + symbol + ')')

# 6. Close the cursor and connection
elements.close()
connection.close()

