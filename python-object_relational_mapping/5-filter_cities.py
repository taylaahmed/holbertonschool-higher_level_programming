#!/usr/bin/python3
"""List all cities from SQL"""

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
    cur.execute("SELECT cities.name "
                "FROM cities "
                "INNER JOIN states on cities.state_id = states.id "
                "WHERE states.name = %s "
                "ORDER BY cities.id ASC ",
                (search,))
    rows = cur.fetchall()
    print(", ".join(row[0] for row in rows))
    cur.close()
    db.close()
