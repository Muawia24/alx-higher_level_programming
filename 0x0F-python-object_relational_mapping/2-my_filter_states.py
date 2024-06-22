#!/usr/bin/python3
"""
script that takes in an argument and displays all values in
the states table of hbtn_0e_0_usa where name matches the argument.
"""

import MySQLdb
from sys import argv

# The code should not be executed when imported
if __name__ == "__main__":

    # make a connection to the database
    connection = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                                 passwd=argv[2], db=argv[3], charset="utf8")
    cur = connection.cursor()
    cur.execute("SELECT * FROM states\
            WHERE name='{}' ORDER BY states.id".format(argv[4]))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    connection.close()
