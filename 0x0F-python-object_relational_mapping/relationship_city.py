#!/usr/bin/python3
"""Write a python file that contains the class definition of a City
"""


from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class City(Base):
    """city"""
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True)
    name = Column(String(125), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
