#!/usr/bin/env python3
#selecting states from databases using mysql alchemy
from sqlalchemy import ceate_engine

engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format("root", "root", "hbtn_0e_0_usa"), pool_pre_ping=True)

session = Session(engine)
for state in session.query(State).order_by(State.id).all(): 
    print("{}: {}".format(state.id, state.name))
session.close()
