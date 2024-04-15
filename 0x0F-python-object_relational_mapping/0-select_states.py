#!/usr/bin/python3
import MySQLdb
import sys
import os
"""a script that lists all states from the database hbtn_0e_0_usa"""


if __name__ == "__main__":
    """Connect to MySQL server"""
    db = MySQLdb.connect(host="localhost", port=3306, user="root",
                         passwd="root", db="hbtn_0e_0_usa")

    """Create a cursor object"""
    cursor = db.cursor()

    """Execute the query to fetch all states"""
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    """clear the console"""
    os.system('cls' if os.name == 'nt' else 'clear')

    """Print the states"""
    for state in cursor.fetchall():
        print(state)

    """Close cursor and database connection"""
    cursor.close()
    db.close()
