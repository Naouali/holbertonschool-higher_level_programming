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
    c.execute("""SELECT * FROM states ORDER BY id ASC""")
    st = c.fetchall()
    arg = sys.argv[4]
    for s in st:
        if str(arg) in s:
            print(s)
    c.close()
    db.close()
