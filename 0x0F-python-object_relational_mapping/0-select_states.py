#!/usr/bin/python3
import MySQLdb
import sys
"""a script that lists all states from the database hbtn_0e_0_usa"""


if __name__ == "__main__":
    """Connect to MySQL server"""
    conn = MySQLdb.connect(host="localhost", port=3306, user="root",
                         passwd="root", db="hbtn_0e_0_usa")

    """Create a cursor object"""
    cur = conn.cursor()

    """Execute the query to fetch all states"""
    cur.execute("SELECT * FROM states ORDER BY id ASC")

    """query states"""
    states = cur.fetchall()

    """Print the states"""
    for state in states:
        print(state)

    """Close cursor and database connection"""
    cur.close()
    conn.close()
