#!/usr/bin/python3
"""
module to list
cities of states
"""

if __name__ == "__main__":
    import MySQLdb
    import sys
    db = MySQLdb.connect(host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3])
    c = db.cursor()
    c.execute('SELECT cities.name FROM cities\
        INNER JOIN states\
        ON cities.state_id=states.id\
        WHERE states.name = %s\
        ORDER BY cities.id ASC', (sys.argv[4],))
    res = c.fetchall()
    if len(res) == 0:
        print("")
    for x in range(len(res)):
        if x < len(res) - 1:
            print(res[x][0] + ", ", end="")
        else:
            print(res[x][0])
