#!/usr/bin/python3
"""
module to fetch
precise data
"""


from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import sys
if __name__ == "__main__":
    e = create_engine("mysql://{}:{}@localhost:3306/{}".format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(e)
    Session = sessionmaker()
    Session.configure(bind=e)
    session = Session()
    res = session.query(State).order_by(State.id).first()
    if res is None:
        print("Nothing")
    else:
        print("{:d}: {:s}".format(res.id, res.name))
