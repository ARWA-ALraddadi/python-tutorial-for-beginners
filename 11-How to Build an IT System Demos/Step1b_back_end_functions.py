#----------------------------------------------------------------
#
# Back-End Functions
#
# These are the back-end functions that get data from the
# database and their unit tests.  Note that since the
# database is updated annually, we need to document which
# version of the database is relevant for the tests.
#
# Although this program has all the functionality needed,
# it has no user interface and is thus not suitable for
# end users.
#
# Also note that these functions are fragile.  They will
# raise exceptions if, for instance, the database server
# cannot be accessed, or if the Movie Survey database is
# not loaded into the server.
#


#----------------------------------------------------------------
# Unit tests for the back-end functions, assuming we are using
# the Movie Survey database dumped on 2013-09-14 18:45:55.
#
"""
To save space, we just print the first part of the results in the
first two tests

>>> print(popular_actors()[:222])
859: Tom Hanks
598: Harrison Ford
547: Robert DeNiro
503: Al Pacino
483: Sean Connery
416: Tom Cruise
410: Mel Gibson
381: Nicolas Cage
376: Julia Roberts
348: Denzel Washington
319: Jodie Foster
309: Arnold Schwarzenegger

>>> print(productive_actors()[:194])
John Wayne (62)
Dennis Hopper (60)
Gene Hackman (59)
Christopher Lee (55)
Samuel L. Jackson (55)
Christopher Walken (54)
Alec Baldwin (53)
Harvey Keitel (53)
Clint Eastwood (52)
James Woods (52)

>>> print(actors_starring_in_a_movie('Arsenic and Old Lace'))
Cary Grant
Peter Lorre

>>> print(actors_starring_in_a_movie('The Great Race'))
Jack Lemmon
Natalie Wood
Peter Falk
Tony Curtis

>>> print(actors_starring_in_a_movie('Unmade Movie'))
No actors found

>>> print(movies_starring_an_actor('Natalie Wood'))
Bob & Carol & Ted & Alice
Gypsy
Kings Go Forth
Marjorie Morningstar
Meteor
Miracle on 34th Street
Rebel Without a Cause: Special Edition
Splendor in the Grass
The Ghost and Mrs. Muir
The Great Race
The Star
This Property Is Condemned
West Side Story

>>> print(movies_starring_an_actor('Lillian Gish'))
Broken Blossoms
Commandos Strike at Dawn
Duel in the Sun
Follow Me
Orphans of the Storm
Portrait of Jennie
Sweet Liberty
The Birth of a Nation
The Night of the Hunter
The Unforgiven
The Whales of August
Way Down East

>>> print(movies_starring_an_actor('Joe Unknown'))
No movies found
"""


#----------------------------------------------------------------
# A function to support unit testing of the back-end
# functions.  Make sure you run this whenever any change
# is made to the back-end functions!
#
def run_unit_tests():
    from doctest import testmod, REPORT_ONLY_FIRST_FAILURE
    print(testmod(verbose = False,
                  optionflags = REPORT_ONLY_FIRST_FAILURE))


#----------------------------------------------------------------
# Import necessary external modules
#

# Import the SQLite functions
from sqlite3 import *


#----------------------------------------------------------------
#
# These are the back-end functions that access the database
# and process the results returned.  Each one returns a
# single string suitable for display in the front-end GUI.
# The signatures of these functions are the agreed-upon interface
# connecting the two development teams.
#

#-----
# Find all actors starring in a given movie
#
def actors_starring_in_a_movie(movie_name):
    # Connect to the "movie survey" database
    connection = connect(database='movie_survey.db')
    movies_db = connection.cursor()
    # Define an appropriate SQL query
    query = """SELECT actor FROM actors_movies
               WHERE movie = '""" + movie_name + """'
               ORDER BY actor"""
    # Initialise the results
    results = ''
    # Execute the query
    movies_db.execute(query)
    # Format the results, if any
    for row in movies_db.fetchall():
        results += row[0] + '\n'
    if results == '':
        results = 'No actors found'
    else:
        results = results[:-1] # delete final newline char
    # Unlock the database
    movies_db.close()
    connection.close()
    # Return the results
    return results

#-----
# Find all movies starring a given actor
#
def movies_starring_an_actor(actors_name):
    # Connect to the "movie survey" database
    connection = connect(database='movie_survey.db')
    movies_db = connection.cursor()
    # Define an appropriate SQL query
    query = """SELECT movie FROM actors_movies
               WHERE actor = '""" + actors_name + """'
               ORDER BY movie"""
    # Initialise the results
    results = ''
    # Execute the query
    movies_db.execute(query)
    # Format the results, if any
    for row in movies_db.fetchall():
        results += row[0] + '\n'
    if results == '':
        results = 'No movies found'
    else:
        results = results[:-1] # delete final newline char
    # Unlock the database
    movies_db.close()
    connection.close()
    # Return the results
    return results

#-----
# Return all actors in order of their "productivity", i.e., the
# number of movies the actors have appeared in.
#
def productive_actors():
    # Connect to the "movie" database (put your login credentials here!)
    # Connect to the "movie survey" database
    connection = connect(database='movie_survey.db')
    movies_db = connection.cursor()
    # Define an appropriate SQL query
    query = """SELECT actor, number_of_movies FROM actors
               ORDER BY number_of_movies DESC, actor ASC"""
    # Execute the query
    movies_db.execute(query)
    # Format the results, if any
    results = ''
    for row in movies_db.fetchall():
        results += row[0] + ' (' + str(row[1]) + ')\n'
    if results == '':
        results = 'No actors found'
    else:
        results = results[:-1] # delete final newline char
    # Unlock the database
    movies_db.close()
    connection.close()
    # Return the results
    return results

#-----
# Return all actors in order of their "popularity", measured by
# the number of people who voted for them in the movie survey.
#
def popular_actors():
    # Connect to the "movie survey" database
    connection = connect(database='movie_survey.db')
    movies_db = connection.cursor()
    # Define an appropriate SQL query
    query = """SELECT actor, count(actor) FROM favorite_actors
               GROUP BY actor
               ORDER BY count(actor) DESC, actor ASC"""
    # Execute the query
    movies_db.execute(query)
    # Format the results, if any
    results = ''
    for row in movies_db.fetchall():
        results += str(row[1]).rjust(3) + ': ' + row[0] + '\n'
    if results == '':
        results = 'No actors found'
    else:
        results = results[:-1] # delete final newline char
    # Unlock the database
    movies_db.close()
    connection.close()
    # Return the results
    return results