#!/usr/bin/python3
"""
list all states
"""

if __name__ == "__main__":
    from MySQLdb import _mysql
    import MySQLdb
    import sys
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        db=sys.argv[3],
        passwd=sys.argv[2],
        user=sys.argv[1])
    c = db.cursor()
    c.execute("""SELECT * FROM states \
            WHERE states.name=%s\
            ORDER BY id ASC""", (sys.argv[4],))
    st = c.fetchall()
    for s in st:
        print(s)
    c.close()
    db.close()
