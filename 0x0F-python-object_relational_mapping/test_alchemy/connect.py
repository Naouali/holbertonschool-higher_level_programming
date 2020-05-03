#!/usr/bin/python3

from sqlalchemy import create_engine
engine = create_engine('mysql:///bank')
res = engine.execute("select * from users")
for x in res:
    print(x)
