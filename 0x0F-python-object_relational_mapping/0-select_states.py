#!/usr/bin/env python3
#selecting states from databases using mysql alchemy
from sqlalchemy import engine

engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format("root", "root", "my_db"), pool_pre_ping=True)
Base.metadata.create_all(engine)

session = Session(engine)
for state in session.query(State).order_by(State.id).all(): 
    print("{}: {}".format(state.id, state.name))
session.close()
