#!/usr/bin/python3
import MySQLdb
import sys
"""a script that lists all states from the database hbtn_0e_0_usa"""


def list_states(username, password, database):
    """Connect to MySQL server"""
    db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database)

    """Create a cursor object"""
    cursor = db.cursor()

    """Execute the query to fetch all states"""
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    """Fetch all rows"""
    states = cursor.fetchall()

    """Print the states"""
    for state in states:
        print(state)

    """Close cursor and database connection"""
    cursor.close()
    db.close()
