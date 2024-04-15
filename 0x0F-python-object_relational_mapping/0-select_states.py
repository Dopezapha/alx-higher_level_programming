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

    """Initialize a set to keep track of printed states"""
    printed_state_names = set()

    """Print the states"""
    for state in states:
        state_name = state[1]
        if state_name not in printed_state_names:
            print(state)
            printed_state_names.add(state_name)

    """Close cursor and database connection"""
    cur.close()
    conn.close()
