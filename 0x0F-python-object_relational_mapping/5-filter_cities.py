#!/usr/bin/python3
"""
script that lists all cities from the database hbtn_0e_0_usa

"""

import MySQLdb
from sys import argv

if __name__ == "__main__":

    connection = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                                 passwd=argv[2], db=argv[3], charset="utf8")
    cur = connection.cursor()
    cur.execute("SELECT cities.id, cities.name FROM cities\
            INNER JOIN states ON cities.state_id = states.id\
            WHERE states.name = %s ORDER BY cities.id", [argv[4], ])
    rows = cur.fetchall()
    cities = []
    for row in rows:
        cities.append(row[1])
    print(", ".join(cities))
    cur.close()
    connection.close()
