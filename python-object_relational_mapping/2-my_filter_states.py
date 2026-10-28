#!/usr/bin/python3
"""search states"""

import sys

import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
    )
    search = sys.argv[4]
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE %s ORDER BY id",
                (search,))
    for row in cur.fetchall():
        print(row)
    cur.close()
    db.close()
