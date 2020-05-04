#!/usr/bin/python3
"""
module to fetch
all states
"""


from model_state import Base, State
from sqlalchemy import (create_engine)
import sys
engine = create_engine("mysql://{}:{}@localhost:3306/{}".format(
    sys.argv[1], sys.argv[2], sys.argv[3]))
res = engine.execute("SELECT id, name FROM states ORDER BY\
        states.id ASC")

for x in res:
    print("{}: {}".format(x[0], x[1]))
