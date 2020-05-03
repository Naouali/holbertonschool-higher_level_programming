#!/usr/bin/python3
"""
create a base
module
"""


from sqlalchemy import Column, Integer,String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
class State(Base):
    """
    state class
    """
    __table__ = "states"
    id = Column(Integer, 
            autoincrement=True,
            unique=True,
            nullable=False, 
            primary_key=True)
    name = Column(String(128),
            nullable=True)
