#!/usr/bin/python3
"""Script that lists all states with a name starting with 'N' from the db"""
import MySQLdb
import sys


if __name__ == "__main__":
    """Connect to MySQL server and list all states starting with 'N'"""
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])

    """Create a cursor object"""
    cur = db.cursor()

    """Execute the query to fetch states starting with 'N'"""
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")

    """Fetch all rows"""
    rows = cur.fetchall()

    """Print the states"""
    for row in rows:
        print(row)

    """Close cursor and database connection"""
    cur.close()
    db.close()
