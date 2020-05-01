#!/usr/bin/python3
"""
list all states
"""


from MySQLdb import _mysql
import MySQLdb
import sys
db = MySQLdb.connect(
        host="localhost",
        port=3306, 
        db=sys.argv[3],
        passwd=sys.argv[2],
        user = sys.argv[1])
c = db.cursor()
c.execute("""SELECT * FROM states ORDER BY id ASC""")
st = c.fetchall()
for s in st:
    print(s)
c.close()
db.close()
