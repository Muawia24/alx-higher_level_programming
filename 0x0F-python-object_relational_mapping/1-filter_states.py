#!/usr/bin/python3
"""
script that lists all states with a
name starting with N (upper N) from
the database hbtn_0e_0_usa.
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":

    connection = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                                 passwd=argv[2], db=argv[3], charset="utf8")
    cur = connection.cursor()
    cur.execute("""SELECT * FROM states
            WHERE states.name LIKE BINARY 'N%' ORDER BY states.id""")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    connection.close()
